from django.db import models
from datetime import datetime


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    create_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name