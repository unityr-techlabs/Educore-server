from django.contrib import admin
from . import models
import nested_admin

# Register your models here.

class IndividualTaskSubmissionInline(admin.StackedInline):
    model = models.IndividualTaskSubmission
    extra = 1
    fields = ('student', 'remarks', 'mark', 'date_of_submission', 'status')
    readonly_fields = ('date_of_submission',)


@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    inlines = [IndividualTaskSubmissionInline]

    list_display = ('topic_name', 'task_type', 'subject', 'classroom', 'last_date')
    list_filter = ('task_type', 'last_date')
    search_fields = ('topic_name', 'description', 'subject__name')
    ordering = ('-last_date',)