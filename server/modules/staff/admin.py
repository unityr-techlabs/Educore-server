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
