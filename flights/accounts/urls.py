from django.urls  import path
from .views import registration, login_page,logout_page, search_flights , list_of_flights, my_bookings,bookings

urlpatterns = [
    path('register/',registration,name='register'),
    path('login/',login_page),
    path('logout/',logout_page),
    path('search_flights/',search_flights,name='search_flights'),
    path('list_of_flights/',list_of_flights),
    path('bookings/<int:id>/', bookings, name='bookings'), 
    path('my_bookings/',my_bookings)
]