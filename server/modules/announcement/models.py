from django.db import models
from classroom import models as classroom_models
from staff import models as staff_models
from students import models as students_models

# Create your models here.
class ClassroomAnnouncement(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    last_date = models.DateField(null=True,blank=True)
    classroom = models.ManyToManyField(classroom_models.ClassRoom, verbose_name='Classroom')

    class Meta:
        verbose_name = 'Classroom Announcement'
        verbose_name_plural = 'Classroom Announcements'

    def __str__(self):
        return f"{self.title} - {self.classroom}"
    
class StaffAnnouncement(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    last_date = models.DateField(null=True,blank=True)
    designation = models.ManyToManyField(staff_models.Designation, verbose_name='Designation')

    class Meta:
        verbose_name = 'Staff Announcement'
        verbose_name_plural = 'Staff Announcements'

    def __str__(self):
        return f"{self.title}"
    
class StudentAnnouncement(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    last_date = models.DateField(null=True,blank=True)
    students = models.ManyToManyField(students_models.Student, verbose_name='Students')

    class Meta:
        verbose_name = 'Student Announcement'
        verbose_name_plural = 'Student Announcements'

    def __str__(self):
        return f"{self.title}"