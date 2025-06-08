from django.contrib import admin
from . import models
import nested_admin


class SubjectInline(admin.StackedInline):
    model = models.Subject
    extra = 1

@admin.register(models.Group)
class GroupAdmin(admin.ModelAdmin):
    inlines = [SubjectInline]
    search_fields = ('id', 'name', 'subject_group__name')
    list_filter = ('subject_group__name',)

