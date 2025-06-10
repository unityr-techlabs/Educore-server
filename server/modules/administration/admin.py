from django.contrib import admin
from . import models
import nested_admin

# Register your models here.

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    search_fields= ('username','first_name','last_name')


@admin.register(models.Designation)
class DesignationAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    search_fields = ('name',)