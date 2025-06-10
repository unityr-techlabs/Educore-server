from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    USER_CHOICES = [
        ('staff','Staff'),
        ('student','Student')
    ]

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('O+', 'O+'), ('O-', 'O-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
    ]

    user_type = models.CharField(default='staff', max_length=50, choices=USER_CHOICES)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField(default=timezone.now)
    age = models.PositiveIntegerField(null=True, blank=True)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES, default='O+')
    temporary_address = models.TextField(verbose_name='Temporary Address',default=None, null=True, blank=True)
    permenent_address = models.TextField(verbose_name='Permenent Address',default=None, null=True, blank=True)
    contact_number = models.IntegerField(verbose_name='Contact Number',default=None, null=True, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Created By')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'
        

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.user_type}"
    
class Designation(models.Model):
    name = models.CharField(max_length=200, verbose_name='Designation Name')
    description = models.TextField(verbose_name='Description')

    class Meta:
        verbose_name = 'Designation'
        verbose_name_plural = 'Designations'

    def __str__(self):
        return f"{self.name}"