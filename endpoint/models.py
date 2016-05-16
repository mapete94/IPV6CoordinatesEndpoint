from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Coordinates(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    count = models.IntegerField(default=0)

    class Meta:
        ordering = ('-count',)
