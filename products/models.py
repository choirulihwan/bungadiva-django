from django.db import models
from datetime import datetime
from enum import Enum

from categories.models import Category


class StatusChoice(Enum):
    READY = "Ready"
    SOLDOUT = "Soldout"

# Create your models here.
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    READY = "Ready"
    SOLDOUT = "Soldout"
    status_choice = (
        (READY, 'Ready'),
        (SOLDOUT, 'Soldout')
    )
    status = models.CharField(max_length=10, choices=status_choice, default=READY)
    #status2 = models.CharField(max_length=10, choices=[(tag, tag.value) for tag in StatusChoice], blank=True)
    #is_available = models.BooleanField(default=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    is_published = models.BooleanField(default=True)
    create_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name