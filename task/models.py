from django.db import models
from django.contrib.auth.models import User


class List(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = 'Lists'

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=250)
    body = models.TextField()
    list = models.ForeignKey(List, related_name='tasks', on_delete=models.CASCADE)
    start_time = models.DateField()
    end_time = models.DateField()
    is_complete = models.BooleanField(default=False)
    author = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
