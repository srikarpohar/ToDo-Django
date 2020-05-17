from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Todo(models.Model):
    user_id = models.ForeignKey(User,db_column="auth_user_id",default=1,on_delete=models.CASCADE)
    task_title = models.CharField(max_length=200)
    task_description = models.TextField()
    is_important_task = models.BooleanField(default=False)

