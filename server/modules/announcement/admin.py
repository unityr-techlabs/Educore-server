from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.ClassroomAnnouncement)
class ClassroomAnnouncementAdmin(admin.ModelAdmin):
    search_fields = ('classroom',)

@admin.register(models.StaffAnnouncement)
class StaffAnnouncementAdmin(admin.ModelAdmin):
    search_fields = ('designation',)

@admin.register(models.StudentAnnouncement)
class StudentAnnouncementAdmin(admin.ModelAdmin):
    search_fields = ('students',)
