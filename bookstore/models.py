from django.db import models
from django.contrib.auth import get_user_model

class Book(models.Model):
    title = models.CharField(max_length=100)
    writer = models.CharField(max_length=100)
    translator = models.CharField(max_length=100, blank=True)
    publisher = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    price = models.PositiveIntegerField()
    cover = models.ImageField(upload_to='covers', blank=True, null=True)
    owner = models.ForeignKey(get_user_model(), models.PROTECT, default=1)
