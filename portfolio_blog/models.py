from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    description= models.TextField(default='')
    created_at= models.DateTimeField(default=timezone.now())

