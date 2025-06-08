from django.contrib import admin
from . import models
import nested_admin
# Register your models here.
@admin.register(models.Hall)
class HallAdmin(admin.ModelAdmin):
    list_filter = ('series', 'floor')
    search_fields = ('series', 'floor')

@admin.register(models.Section)
class SectionAdmin(admin.ModelAdmin):
    list_filter = ('section_name',)
    search_fields = ('section_name',)

@admin.register(models.ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'standard', 'section', 'nick_name', 'hall_number', 'created_at')
    list_filter = ('standard', 'section', 'created_at')
    search_fields = ('nick_name', 'section__name', 'standard__name') 
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Class Room Details', {
            'fields': ('standard', 'section', 'nick_name', 'hall_number', 'class_teacher', 'assistant_teacher', 'batch_start', 'batch_end'),
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
        }),
    )

class ClassRoomStudentAddableInline(admin.StackedInline):
    model = models.ClassRoomStudentAddable
    extra = 1
    verbose_name = "Student"
    verbose_name_plural = "Students"


@admin.register(models.ClassRoomStudent)
class ClassRoomStudentAdmin(admin.ModelAdmin):
    inlines = [ClassRoomStudentAddableInline]
    list_display = ('id', 'batch_name', 'get_class_room', 'start_date', 'end_date', 'status')
    list_filter = ('status', 'start_date', 'class_room__standard')
    search_fields = ('batch_name', 'class_room__nick_name', 'class_room__section__name')
    readonly_fields = ('created_at', 'updated_at')

    def get_class_room(self, obj):
        return str(obj.class_room)
    get_class_room.short_description = 'Class Room'