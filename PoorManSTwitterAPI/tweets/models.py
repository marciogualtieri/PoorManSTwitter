from django.db import models
from django.utils import timezone


class Tweet(models.Model):

    datetime = models.DateTimeField(default=timezone.now, blank=True)
    message = models.CharField(max_length=50)
    name = models.CharField(max_length=15)

    class Meta:
        unique_together = ["datetime", "name"]
