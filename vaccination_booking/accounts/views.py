from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate ,login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import VaccinationCenter,  Booking
from .forms import BookingForm,CenterSearchForm
from django.utils import timezone

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
            return redirect('/list_of_centre/')  
    return render(request,'login.html')

def logout_page(request):
    User(request)
    return redirect("/login/")

@login_required
def list_of_center(request):
    centers = VaccinationCenter.objects.all()
    return render(request, 'list_of_centre.html', {'centers': centers})

@login_required
def search_center(request):
    centers = None  # Initialize as None
    if request.method == 'POST':
        form = CenterSearchForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            # center_name = form.cleaned_data['center_name']

            centers = VaccinationCenter.objects.filter(
                city__icontains=city,
                # center_name__icontains=center_name
            )
    else:
        form = CenterSearchForm()
    context = {'form': form, 'centers': centers}  
    return render(request, 'search_center.html', context)



@login_required
def book_slot(request, id):
    center = get_object_or_404(VaccinationCenter, pk=id) 
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            num_slot = form.cleaned_data['num_slot']

            if num_slot <= center.available_slots:
                # Create the Booking object
                booking = Booking.objects.create(
                    user=request.user,
                    num_slot=num_slot,
                    booking_date=timezone.now().date()
                )

                center.available_slots -= num_slot
                center.save()

                return redirect('/my_bookings/')  
            else:
                messages.error(request, "Not enough slots available.")
        else:
            messages.error(request, "Invalid form data.")      

    context = {
        'center': center,
        'form': BookingForm(initial={'center': center}), 
    }
    return render(request, 'book_slot.html', context)

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'my_booking.html', {'bookings': bookings})
