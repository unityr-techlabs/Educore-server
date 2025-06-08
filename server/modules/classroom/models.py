from django.db import models
from staff import models as staff_models
from students import models as students_models
from django.core.exceptions import ValidationError
from django.utils import timezone

# Create your models here.
class Section(models.Model):
    section_name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Section'
        verbose_name_plural = 'Sections'
        ordering = ['section_name']

    def __str__(self):
        return self.section_name
    
class Hall(models.Model):
    series = models.CharField(max_length=3, verbose_name='Series Name', help_text='Set series name Eg. M, S...')
    number = models.IntegerField(verbose_name='Hall Number')
    floor = models.IntegerField(verbose_name='Floor')


    class Meta:
        verbose_name = 'Hall'
        verbose_name_plural = 'Halls'

    def __str__(self):
        return f"{self.series}-{self.number} (Floor {self.floor})"    

class ClassRoom(models.Model):
    STANDARD_CHOICES = STANDARD_CHOICES = [(str(i), str(i)) for i in range(1, 13)]

    hall_number = models.ForeignKey(Hall, on_delete=models.CASCADE, verbose_name='Hall')
    standard = models.CharField(max_length=2, choices=STANDARD_CHOICES)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    nick_name = models.CharField(max_length=50, unique=True)
    class_teacher = models.ForeignKey(staff_models.Staff, on_delete=models.CASCADE, related_name='class_teacher', null=True, blank=True)
    assistant_teacher = models.ForeignKey(staff_models.Staff, on_delete=models.CASCADE, related_name='assistant_teacher', null=True, blank=True)
    batch_start = models.DateField(default=timezone.now)
    batch_end = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Class Room'
        verbose_name_plural = 'Class Rooms'
        ordering = ['standard', 'section']

    def clean(self):
        if self.class_teacher and self.class_teacher.status != 'active':
            raise ValidationError(f"Class teacher {self.class_teacher} is not active.")

        if self.assistant_teacher and self.assistant_teacher.status != 'active':
            raise ValidationError(f"Assistant teacher {self.assistant_teacher} is not active.")

        if ClassRoom.objects.filter(standard=self.standard, section=self.section).exclude(pk=self.pk).exists():
            raise ValidationError(f"ClassRoom for standard {self.standard} and section {self.section} already exists.")

    def __str__(self):
        return f"{self.standard} {self.section} - {self.nick_name}"
    
class ClassRoomStudentAddable(models.Model):
    student = models.ForeignKey('students.Student', on_delete=models.CASCADE, related_name='class_room_students')
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE, related_name='classroom',default=None, null=True, blank=True)
    roll_number = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Class Room Student'
        verbose_name_plural = 'Class Room Students'
        unique_together = ('student', 'classroom')

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name} ({self.student.admission_number or 'No Admission Number'})"

