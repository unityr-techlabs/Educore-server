from django.db import models
from accounts import models as user_models
from curriculum import models as curriculam_models
# Create your models here.
  
class Student(models.Model):
    STANDARD_CHOICES = [(str(i), str(i)) for i in range(1, 13)]
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    user = models.ForeignKey(user_models.User,on_delete=models.CASCADE, verbose_name='User')
    admission_date = models.DateField()
    admission_number = models.CharField(max_length=100, unique=True, null=True, blank=True)
    joining_standard = models.CharField(max_length=2, choices=STANDARD_CHOICES)
    current_standard = models.CharField(max_length=2, choices=STANDARD_CHOICES, default='1', null=True, blank=True)
    group = models.ForeignKey(curriculam_models.Group, on_delete=models.CASCADE, null=True, blank=True)
    father_name = models.CharField(max_length=100, null=True, blank=True)
    mother_name = models.CharField(max_length=100, null=True, blank=True)
    guardian_name = models.CharField(max_length=100, null=True, blank=True)
    phone_primary = models.CharField(max_length=15)
    phone_secondary = models.CharField(max_length=15, null=True, blank=True)
    address_permanent = models.TextField()
    address_temporary = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} ({self.admission_number or 'No Admission Number'})"
