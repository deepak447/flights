from django import forms
from .models import Flight, Booking

# For searching flights
class FlightSearchForm(forms.Form):
    departure_city = forms.CharField(max_length=50)
    arrival_city = forms.CharField(max_length=50)
    departure_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

# For booking a flight 
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['flight', 'num_passengers']
    