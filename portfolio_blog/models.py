from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    description= models.TextField(default='')
    created_at= models.DateTimeField(default=timezone.now())

class Users(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    email = models.CharField(max_length=100, blank=True, default='')
    phone = models.CharField(max_length=100, blank=True, default='')
    username = models.CharField(max_length=100, blank=True, default='')
    password = models.CharField(max_length=100, blank=True, default='')
    created_at= models.DateTimeField(default=timezone.now())

