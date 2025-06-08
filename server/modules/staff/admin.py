from django.contrib import admin
from . import models
import nested_admin

# Register your models here.

@admin.register(models.Staff)
class StaffAdmin(nested_admin.NestedModelAdmin):
    
    list_filter = (
        'status', 'joining_designation', 'staff__gender',
        'staff__blood_group', 'created_at', 'updated_at',
    )
    search_fields = (
        'staff__first_name', 'staff__last_name', 'phone_primary',
        'phone_secondary', 'email',
    )

class InduvidualStaffAttendanceInline(admin.StackedInline):
    model = models.InduvidualStaffAttendance
    extra = 1


class StaffAttendanceAdmin(admin.ModelAdmin):
    inlines = [InduvidualStaffAttendanceInline]


admin.site.register(models.StaffAttendance, StaffAttendanceAdmin)

@admin.register(models.StaffLeave)
class StaffLeaveAdmin(admin.ModelAdmin):
    list_display = (
        'staff',
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
        'staff__first_name',
        'staff__last_name',
        'leave_type',
        'reason',
    )
    readonly_fields = (
        'created_at',
        'updated_at',
    )
    ordering = ('-created_at',)
