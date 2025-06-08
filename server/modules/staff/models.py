from django.db import models
from accounts import models as user_models
from staff import models as staff_models

# Create your models here.

class Designation(models.Model):
    name = models.CharField(max_length=200, verbose_name='Designation Name')
    description = models.TextField(verbose_name='Description')

    class Meta:
        verbose_name = 'Designation'
        verbose_name_plural = 'Designations'

    def __str__(self):
        return f"{self.name}"

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
    joining_designation = models.ForeignKey(Designation, default=None, on_delete=models.CASCADE, verbose_name='Select Designation', null=True, blank=True)
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
    

class StaffAttendance(models.Model):
    date = models.DateField()

    class Meta:
        verbose_name = 'Staff Attendance'

    def __str__(self):
        return f"Staff attendance - {self.date}"

class InduvidualStaffAttendance(models.Model):
    ATTENDANCE_STATUS_CHOICES = [
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('late', 'Late'),
        ('excused', 'Excused'),
        ('pending', 'Pending'),
    ]

    staff_attendance = models.ForeignKey(StaffAttendance,on_delete=models.CASCADE,related_name='staff_attendance')
    staff = models.ForeignKey(staff_models.Staff,on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=255,choices=ATTENDANCE_STATUS_CHOICES,default='Pending')

    class Meta:
        verbose_name = 'Individual Staff Attendance'
        verbose_name_plural = 'Individual Staff Attendances'

    def __str__(self):
        return f"{self.staff.first_name} {self.staff.last_name} - {self.status}"
    
class StaffLeave(models.Model):
    staff = models.ForeignKey(staff_models.Staff, on_delete=models.CASCADE, related_name='leaves')
    leave_type = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('approved', 'Approved'), ('pending', 'Pending'), ('rejected', 'Rejected')], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Staff Leave'
        verbose_name_plural = 'Staff Leaves'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.staff.first_name} {self.staff.last_name} - {self.leave_type} ({self.start_date} to {self.end_date})"
    

