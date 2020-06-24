from django.db import models


class Urls(models.Model):
    targetURL = models.CharField(max_length=100)
    hash = models.CharField(max_length=15, null=True, blank=True)
    shrinkedURL = models.CharField(max_length=100, null=True, blank=True, unique=True)
