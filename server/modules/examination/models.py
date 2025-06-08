from django.db import models
from classroom import models as classroom_models
from curriculum import models as curriculum_models
from students import models as students_models

# Create your models here.
class ExamSubject(models.Model):
    subject = models.ForeignKey(curriculum_models.Subject, on_delete=models.CASCADE, related_name='exam_subjects')
    exam = models.ForeignKey('Exam', on_delete=models.CASCADE, related_name='subjects')
    date = models.DateField(default=None, null=True, blank=True)
    max_marks = models.PositiveIntegerField(default=100)
    passing_marks = models.PositiveIntegerField(default=35)

    class Meta:
        verbose_name = 'Exam Subject'
        verbose_name_plural = 'Exam Subjects'
        unique_together = ('subject', 'exam')
        ordering = ['date', 'subject__name']

    def __str__(self):
        return f"{self.subject.name} for {self.exam.exam_name}"
    
class Exam(models.Model):
    EXAM_TYPE_CHOICES = [
        ('unit_test', 'Unit Test'),
        ('mid_term', 'Mid Term'),
        ('final_exam', 'Final Exam'),
        ('other', 'Other'),
    ]

    TERM_CHOICES = [
        ('first_term', 'First Term'),
        ('second_term', 'Second Term'),
        ('third_term', 'Third Term')
    ]

    term = models.CharField(max_length=20, choices=TERM_CHOICES, default='first_term')
    exam_name = models.CharField(max_length=100)
    exam_type = models.CharField(max_length=20, choices=EXAM_TYPE_CHOICES)
    start_date = models.DateField(default=None, null=True, blank=True)
    end_date = models.DateField(default=None, null=True, blank=True)
    class_room = models.ForeignKey(classroom_models.ClassRoom, on_delete=models.CASCADE, related_name='exams')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Exam'
        verbose_name_plural = 'Exams'
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.exam_name} ({self.exam_type}) - {self.class_room}"
    
class ExamResult(models.Model):
    student = models.ForeignKey(students_models.Student, on_delete=models.CASCADE, related_name='exam_results')
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='results',default=None, null=True, blank=True)
    

    class Meta:
        verbose_name = 'Exam Result'
        verbose_name_plural = 'Exam Results'
        unique_together = ['student']

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name} - {self.exam.exam_name}"
    
class ResultSubject(models.Model):
    ATTENDANCE_STATUS_CHOICES = [
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('late', 'Late'),
        ('excused', 'Excused'),
        ('pending', 'Pending'),
    ]

    RESULT_CHOICES = [
        ('pass','Pass'),
        ('fail','Fail')
    ]

    exam_subject = models.ForeignKey(ExamSubject, on_delete=models.CASCADE,verbose_name='Subject', related_name='results')
    exam_result = models.ForeignKey('ExamResult', on_delete=models.CASCADE, related_name='result_subjects')
    attendance = models.CharField(max_length=10, choices=ATTENDANCE_STATUS_CHOICES, default='absent')
    marks_obtained = models.PositiveIntegerField(default=0)
    result = models.CharField(max_length=50, verbose_name='Result', choices=RESULT_CHOICES, default='pass')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Result Subject'
        verbose_name_plural = 'Result Subjects'
        unique_together = ('exam_subject', 'exam_result')
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.exam_subject.subject.name} - {self.exam_result.student.first_name} {self.exam_result.student.last_name} ({self.exam_subject.max_marks})"


