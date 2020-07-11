from django.utils import timezone

from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    short_name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.short_name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    categories = models.ManyToManyField(Category)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'"{self.title}" by: {self.author.username}'
