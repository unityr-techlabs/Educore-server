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