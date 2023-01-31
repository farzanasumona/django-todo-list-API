from django.db import models
from datetime import datetime

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now)
    update_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

