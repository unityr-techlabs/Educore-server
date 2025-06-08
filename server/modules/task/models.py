from django.db import models
from classroom import models as classroom_models
from curriculum import models as curriculum_models
from django.utils import timezone
from students import models as students_models
# Create your models here.
class Task(models.Model):
    TASK_CHOICES = [
        ('assignment','Assignment'),
        ('homework','Homework'),
        ('project','Project'),
        ('deminar','Seminar')
    ]

    TERM_CHOICES = [
        ('first_term', 'First Term'),
        ('second_term', 'Second Term'),
        ('third_term', 'Third Term')
    ]

    classroom = models.ForeignKey(classroom_models.ClassRoom,on_delete=models.CASCADE,related_name='task_classroom',default=None,null=True,blank=True)
    term = models.CharField(max_length=255,choices=TERM_CHOICES,default='First Term')
    subject = models.ForeignKey(curriculum_models.Subject,on_delete=models.CASCADE,related_name='subject')
    task_type = models.CharField(max_length=255,choices=TASK_CHOICES,default='Homework')
    topic_name = models.CharField(max_length=255)
    description = models.TextField()
    max_marks = models.IntegerField(default=10)
    last_date = models.DateField(default=timezone.now)

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        unique_together = ['subject']

    def __str__(self):
        return f"{self.classroom} - {self.task_type} - {self.subject.name}"
   
class IndividualTaskSubmission(models.Model):
    SUBMISSION_STATUS_CHOICES = [
        ('pending','Pending'),
        ('submitted','Submitted'),
        ('late','Late'),
        ('not_submitted','Not Submitted')
    ]

    tast_submission = models.ForeignKey(Task,on_delete=models.CASCADE,related_name='task_submission')
    student = models.ForeignKey(students_models.Student, on_delete=models.CASCADE, related_name='student_task')
    remarks = models.TextField(default=None,null=True,blank=True)
    mark = models.IntegerField(default=0,null=True,blank=True)
    date_of_submission = models.DateField(default=timezone.now)
    status = models.CharField(max_length=50,choices=SUBMISSION_STATUS_CHOICES,default='Pending')

    class Meta:
        verbose_name = 'Task submission list'

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name}"