from django.contrib import admin
from .models import Flight, Booking

# admin.site.register(Flight)
# admin.site.register(Booking)
@admin.register(Flight) 
class FlightAdmin(admin.ModelAdmin):
    list_display = ('id','flight_number','departure_city','arrival_city','departure_time',
                    'arrival_time','airline','price','seats_available')
    ordering = ['id']
    
@admin.register(Booking) 
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user','flight','num_passengers','booking_date')