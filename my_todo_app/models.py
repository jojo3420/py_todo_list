from django.db import models


# Create your models here.
class Todo(models.Model):
    content = models.CharField(max_length=256)
    is_done = models.BooleanField(default=False)