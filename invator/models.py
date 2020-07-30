from django.db import models

# Create your models here.
"""
Name of client
Type of work done
Amount to be payed
Hours spent (optional)
Amount by hour(if it was an hourly job)
Amount by contract
"""
class Invator(models.Model):
    Name = models.CharField(max_length=255,verbose_name='name')
    Workdone = models.CharField(max_length=255)
    Amount = models.CharField(max_length=255000000)
    Hours = models.CharField(max_length=2500000)
    HourAmount = models.CharField(max_length=255000000)
    ContractAmount = models.CharField(max_length=255000000)
