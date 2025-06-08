from django.contrib import admin
from . import models
import nested_admin

# Register your models here.

@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_filter = (
        'user__gender', 'user__blood_group', 'joining_standard', 'current_standard', 'status', 'created_at', 'updated_at', 'admission_date',
    )
    search_fields = (
        'first_name', 'last_name', 'admission_number',
        'phone_primary', 'phone_secondary', 'guardian_name',
        'father_name', 'mother_name', 'email',
    )
    readonly_fields = ('created_at', 'updated_at')

class IndividualStudentInline(admin.StackedInline):
    model = models.IndividualStudentAttendance
    extra = 1

@admin.register(models.StudentAttendance)
class StudentAttendanceAdmin(admin.ModelAdmin):
    inlines = [IndividualStudentInline]
    list_display = (
        'class_room',
        'date',
    )
    list_filter = (
        'date',
    )
    # search_fields = (
    #     'class_room_batch__class_room',  
    #     'class_room_batch__student__first_name', 
    #     'class_room_batch__student__last_name',
    # )
    readonly_fields = (
        'date',
    )
    ordering = ('-date',)

@admin.register(models.StudentLeave)
class StudentLeaveAdmin(admin.ModelAdmin):
    list_display = (
        'student',
        'leave_type',
        'start_date',
        'end_date',
        'status',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'leave_type',
        'status',
        'start_date',
        'end_date',
    )
    search_fields = (
        'student__first_name',
        'student__last_name',
        'leave_type',
        'reason',
    )
    readonly_fields = (
        'created_at',
        'updated_at',
    )
    ordering = ('-created_at',)
