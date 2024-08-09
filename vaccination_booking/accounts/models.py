from django.db import models
from django.contrib.auth.models import User 


class VaccinationCenter(models.Model):
    city = models.CharField(max_length=255)
    center_name = models.CharField(max_length=255)
    vaccine_name = models.CharField(max_length=255)
    address = models.TextField()
    working_hours_start = models.TimeField()  # Use TimeField for time input
    working_hours_end = models.TimeField()  
    available_slots = models.IntegerField(default=10)
    

    def __str__(self):
        return self.center_name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateField()
    address = models.TextField()
    city = models.CharField(max_length=255)
    centre_name = models.CharField(max_length=255)
    slot = models.CharField(max_length=255)
    num_slot = models.IntegerField()

    def __str__(self):
        return self.centre_name