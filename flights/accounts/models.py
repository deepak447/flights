from django.db import models
from django.contrib.auth.models import User  # For user authentication

class Flight(models.Model):
    flight_number = models.CharField(max_length=10, unique=True)
    departure_city = models.CharField(max_length=50)
    arrival_city = models.CharField(max_length=50)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    airline = models.CharField(max_length=50, blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    seats_available = models.IntegerField(default=60)

    def __str__(self):
        return f"{self.flight_number} - {self.departure_city} to {self.arrival_city}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    num_passengers = models.IntegerField(default=1)
    booking_date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2) 
    airline = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return f"Booking #{self.id} - {self.user.username} - {self.flight.flight_number}" 



 

   

  