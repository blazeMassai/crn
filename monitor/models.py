from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from station.models import Station
from datetime import datetime

class Crn(models.Model):
    cr_station = models.ForeignKey(Station, on_delete=models.DO_NOTHING)
    crn_comm_date = models.DateField(auto_now_add=False, auto_now=False)
    crn_clos_date = models.DateField(auto_now_add=False, auto_now=False)
    cr_note = models.CharField(max_length=250, blank=False)
    cr_cash = models.IntegerField()
    cr_status = models.CharField(max_length=250, default='Delivered', editable=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)

    def get_absolute_url(self):
        return reverse("crn_detail" ,kwargs={'pk':self.pk})



    def __str__(self):
        return self.cr_note
