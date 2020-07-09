from django.utils import timezone

from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)


class Category(models.Model):
    short_name = models.CharField(max_length=100)
    description = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING)
