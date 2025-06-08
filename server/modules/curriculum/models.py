from django.db import models

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=255, verbose_name='Group SSC or SSLC and HSC', help_text='Until SSLC or SSC')

    class Meta:
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'

    def __str__(self):
        return f"{self.name}"
  
class Subject(models.Model):
    name = models.CharField(max_length=50, verbose_name='Subject Name', help_text='Type subject name Eg. Tamil, English...')
    description = models.TextField(verbose_name='Subject Description', help_text="Write few words about the subject")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name='Group', related_name='subject_group')

    class Meta:
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'

    def __str__(self):
        return f"{self.name}"