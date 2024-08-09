from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate ,login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import FlightSearchForm, BookingForm
from .models import Flight, Booking
# Create your views here.

def registration(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.info(request, 'User already exists')
            
        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
        )
        user.set_password(password)
        user.save()
        return redirect('/login/')
    return render(request, 'register.html')

def login_page(request): 
    if request.method == 'POST':
        username = request.POST.get('user_name')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
                messages.error(request, 'invalid user name')
                return redirect('/login/')
        user = authenticate(username = username , password = password)
        if user is None:
            messages.error(request, 'invalid password')
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/my_bookings/')  
    return render(request,'login.html')

def logout_page(request):
    User(request)
    return redirect("/login/")
@login_required
def search_flights(request):
    flights = None
    if request.method == 'POST':
        form = FlightSearchForm(request.POST)
        if form.is_valid():
            departure_city = form.cleaned_data['departure_city']
            arrival_city = form.cleaned_data['arrival_city']
            departure_date = form.cleaned_data['departure_date']

            flights = Flight.objects.filter(
                departure_city__icontains=departure_city,
                arrival_city__icontains=arrival_city,
                departure_time__date=departure_date 
            )
            if not flights: 
                if departure_city and arrival_city:
                    message = f"No flights found from {departure_city} to {arrival_city} on {departure_date.strftime('%Y-%m-%d')}."
                elif departure_city:
                    message = f"No flights found from {departure_city} on {departure_date.strftime('%Y-%m-%d')}."
                elif arrival_city:
                    message = f"No flights found to {arrival_city} on {departure_date.strftime('%Y-%m-%d')}."
                # else:
                #     message = f"No flights found"
                messages.info(request, message)
    else:
        form = FlightSearchForm()
    context = {'form': form, 'flights': flights}
    return render(request, 'search_flight.html', context)

@login_required
def list_of_flights(request): 
    if not request.user.is_authenticated:
        return redirect('/login/') 
    flights = Flight.objects.all()
    return render(request, 'list_of_flights.html', {'flights':flights})


@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'my_booking.html', {'bookings': bookings})

@login_required
def bookings(request, id):
    flight = get_object_or_404(Flight, pk=id)
    # Handle booking submission
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            num_passengers = form.cleaned_data['num_passengers']
            # Check for available seats
            if num_passengers <= flight.seats_available:
                booking = Booking.objects.create(
                    user=request.user,
                    flight=flight,
                    num_passengers=num_passengers,
                     
                )

                flight.seats_available -= num_passengers
                flight.save()

                return redirect('/my_bookings/')  
            else:
                messages.error(request, "Not enough seats available.")
        else:
            messages.error(request, "Invalid form data.")

    context = {
        'flight': flight,
        'form': BookingForm(initial={'flight': flight}), 
    }
    return render(request, 'booking.html', context)