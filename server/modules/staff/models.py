from django.db import models
from accounts import models as user_models
# Create your models here.

class Staff(models.Model):
    DESIGNATION_CHOICES = [
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
        ('accountant', 'Accountant'),
        ('librarian', 'Librarian'),
        ('other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]
    
    staff = models.ForeignKey(user_models.User ,on_delete=models.CASCADE, verbose_name='Staff', default=None, related_name='staff')
    joining_date = models.DateField()
    joining_designation = models.CharField(max_length=20, choices=DESIGNATION_CHOICES)
    phone_primary = models.CharField(max_length=15)
    phone_secondary = models.CharField(max_length=15, null=True, blank=True)
    address_permanent = models.TextField()
    address_temporary = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Staff'
        verbose_name_plural = 'Staffs'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.staff.first_name} {self.staff.last_name} ({self.joining_designation})"
    

