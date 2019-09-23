
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Station(models.Model):
    station_name = models.CharField(max_length=300, blank=False)

    def __str__(self):
        return self.station_name
