from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    description= models.TextField(default='')
    created_at= models.DateTimeField(default=timezone.now())
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=2)
    category = models.CharField(max_length=100, blank=True, default='random')

class Comments(models.Model):
    comment= models.TextField(default='')
    created_at= models.DateTimeField(default=timezone.now())
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=2)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=1)

