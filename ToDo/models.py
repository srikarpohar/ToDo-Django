from django.db import models

# Create your models here.

class Todo(models.Model):
    task_title = models.CharField(max_length=200)
    task_description = models.TextField()
    is_important_task = models.BooleanField(default=False)

