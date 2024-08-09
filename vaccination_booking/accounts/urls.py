from django.urls import path
from .views import registration, login_page,list_of_center,search_center,my_bookings,book_slot

urlpatterns = [
    path('register/',registration,name='register'),
    path('login/',login_page),
    path('list_of_centre/',list_of_center),
    path('search_center/',search_center),
    path('my_bookings/',my_bookings),
    path('book_slot/<int:id>/', book_slot, name='bookings'),
]