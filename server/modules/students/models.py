from django.db import models
from administration import models as user_models
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

class StudentAttendance(models.Model):
    ATTENDANCE_STATUS_CHOICES = [
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('late', 'Late'),
        ('excused', 'Excused'),
        ('pending', 'Pending'),
    ]

    class_room = models.ForeignKey('classroom.ClassRoom', on_delete=models.CASCADE, related_name='attendances',default=None, null=True, blank=True)
    date = models.DateField(auto_now_add=True,verbose_name='Attendance Date')
    

    class Meta:
        verbose_name = 'Attendance'
        verbose_name_plural = 'Attendances'
        ordering = ['-date']

    def __str__(self):
        return f"{self.class_room_batch}- {self.date}"
    
class IndividualStudentAttendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE,related_name='student_attendance')
    attendance = models.ForeignKey(StudentAttendance, on_delete=models.CASCADE, related_name='individual_attendance')
    status = models.CharField(max_length=30, choices=StudentAttendance.ATTENDANCE_STATUS_CHOICES, default='pending')
    remarks = models.TextField(null=True, blank=True, verbose_name='Remarks')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At')

    class Meta:
        verbose_name = 'Individual Student Attendance'
        verbose_name_plural = 'Individual Student Attendances'
        unique_together = ('student', 'attendance')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name} - {self.attendance.date} ({self.status})"
    
class StudentLeave(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='leaves')
    leave_type = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('approved', 'Approved'), ('pending', 'Pending'), ('rejected', 'Rejected')], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Student Leave'
        verbose_name_plural = 'Student Leaves'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name} - {self.leave_type} ({self.start_date} to {self.end_date})"
    

