from django.db import models

# Create your models here.
class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=1000)
    completed = models.BooleanField(default=False)
