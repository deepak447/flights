from django.contrib import admin
from .models import VaccinationCenter

from django.contrib import admin
from .models import VaccinationCenter, Booking

# admin.site.register(VaccinationCenter)
# admin.site.register(VaccinationSlot)
# admin.site.register(Booking),
@admin.register(VaccinationCenter)
class VaccinationCenterAdmin(admin.ModelAdmin):
    list_display = ('id','city','center_name','vaccine_name','address','working_hours_start', 'working_hours_end',
                    'available_slots')
    ordering = ['id']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id','user','city','booking_date','centre_name','slot')
    ordering = ['id']