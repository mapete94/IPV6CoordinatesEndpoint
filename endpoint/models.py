from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Coordinates(models.Model):
    lattitude = models.FloatField()
    longitude = models.FloatField()
    ipv6start = models.CharField(max_length=100)
    ipv6end = models.CharField(max_length=100)

    class Meta:
        ordering=('ipv6start',)