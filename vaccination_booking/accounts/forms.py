from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['booking_date','num_slot']
        widgets = {
            'booking_date': forms.DateInput(attrs={'type': 'date'}),
       }

class CenterSearchForm(forms.Form):
    city = forms.CharField(max_length=50)
    # center_name = forms.CharField(max_length=50)
    # date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
   