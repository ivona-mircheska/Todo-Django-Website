from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=100)
    task_category = models.CharField(max_length=100)
    task_description = models.CharField(max_length=100)
    task_created = models.DateTimeField(auto_now_add=True)
    task_expiration_date = models.DateTimeField()
    task_priority = models.IntegerField(default=0)
    task_status = models.CharField(max_length=50, default='Pending')

    def __str__(self):
        return (f"{self.task_name} {self.task_category}")
