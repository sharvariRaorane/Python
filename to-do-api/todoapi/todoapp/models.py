from django.db import models
import datetime

# Create your models here.
class TODO(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    date = models.DateField(default=datetime.date.today())
    