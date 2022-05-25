from django.urls import path
from . import views
urlpatterns=[
    path('',views.demoIndex2, name='index2'),
    path('/Home', views.demoIndex, name = 'index'),
    path('/classes',views.demoClass, name='Classes'),
    path('/signIn',views.demoIn, name='sign in'),
    path('/signUp',views.demoUp, name='sign up'),
    path('/contactUs',views.demoContact, name='ContactUs'),
    path('/frequentlyAsked',views.demoFreq, name='frequentlyAsked'),
    path('/Trips',views.demoTrips, name='Trips'),
    path('/aboutUs',views.demoAbout, name='about us'),
    path('/Profile',views.demoProfile, name='profile'),
    #path('/selectSeats',views.demoSeats, name='SelectSeats'),
    path('/details',views.demoDetails, name='details'),
    path('/booked',views.demoBooked, name='bookedtrips'),
    path('/stations',views.demoStations, name='stations'),
    path('/SelectSeats/<int:id>', views.demoSeats, name="seats"),
    path('/update',views.demoupdate, name="update"),
    path('/delete', views.demodelete, name="delete"),
]
