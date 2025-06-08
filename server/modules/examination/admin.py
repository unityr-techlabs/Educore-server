from django.contrib import admin
from . import models
import nested_admin

# Register your models here.
class ExamSubjectInline(admin.StackedInline):
    model = models.ExamSubject
    extra = 1


@admin.register(models.Exam)
class ExamAdmin(admin.ModelAdmin):
    inlines = [ExamSubjectInline]

    list_display = (
        'exam_name',
        'exam_type',
        'term',
        'class_room',
        'start_date',
        'end_date',
        'created_at',
    )
    list_filter = (
        'exam_type',
        'term',
        'class_room',
        'start_date',
    )
    search_fields = (
        'exam_name',
        'class_room__nick_name',
        'class_room__standard',
    )
    ordering = ('-start_date',)
    date_hierarchy = 'start_date'
    readonly_fields = ('created_at', 'updated_at')

class ExamResultSubjectInline(admin.StackedInline):
    model = models.ResultSubject
    extra = 1


@admin.register(models.ExamResult)
class ExamResultAdmin(admin.ModelAdmin):
    inlines = [ExamResultSubjectInline]

    list_display = (
        'student',
        'exam',
    )
    list_filter = (
        'exam',
    )
    search_fields = (
        'student__user__first_name',
        'student__user__last_name',
        'exam__exam_name',
    )
    ordering = ('student__user__last_name',)