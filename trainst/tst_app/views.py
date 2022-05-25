from typing import ContextManager
from django.http.request import validate_host
from django.shortcuts import redirect, render , get_object_or_404
from . models import *

# Create your views here.
def demoIndex(request):
    return render(request,'index.html')
def demoIndex2(request):
    return render(request, 'index2.html')
def demoClass(request):
    context = {
        'trains': Train.objects.all(),
    }

    return render(request,'Classes.html', context)

def demoProfile(request):
    prof_info = User.objects.get(username =email_in)
    context ={
        'prof_user': prof_info.username,
        'prof_pass': prof_info.password, 
        'prof_locat': prof_info.location,
        'prof_email': prof_info.email
    }
    return render(request,'profile.html', context)

def demoContact(request):
    return render(request,'ContactUS.html')
    
def demoFreq(request):
    return render(request,'frequentlyAsked.html')


def demoSeats(request, id) :
    global trip_id , user_trip
    trip_id = Trip.objects.get(id=id)
    user_trip= User.objects.get(username = email_in)
    global num_seats , visa
    if request.method =='POST':

        num_seats = request.POST.get('NoOfSeats')
        visa = request.POST.get('PaymentWay')
        num_seats =int(num_seats)
        if trip_id.seats>=num_seats:
            total = trip_id.seats - num_seats
            trip_id.seats = total
            trip_id.save()
            user_trip.my_trips =trip_id
            user_trip.save()
    return render(request,'SelectSeats.html')

def demoTrips(request):

    search = Trip.objects.all()
    
    Departure_Time =None
    from_station = None
    to_station = None
    Classtrain =None
    from_date = None
    to_date = None
    seats =None
    Price =None
    if 'start_time' in request.GET:
        Departure_Time = request.GET['start_time']
        if Departure_Time:
            search = search.filter(Departure_Time = Departure_Time)
    
    if 'From' in request.GET: 
        from_station = request.GET['From']
        if from_station:
            search = search.filter(from_station = from_station)
            
    if 'to' in request.GET:
        to_station =request.GET['to']
        if to_station:
            search = search.filter(to_station =  to_station)
    if 'trains' in request.GET:
        Classtrain = request.GET['trains']   
        if Classtrain:
            search = search.filter(Classtrain=Classtrain)  
    if 'from_date' in request.GET:
        from_date = request.GET['from_date']
        if from_date:
            search = search.filter(from_date = from_date)
    if 'to_date' in request.GET:
        to_date = request.GET['to_date']
        if to_date:
            search = search.filter(to_date = to_date)  
    if 'seats' in request.GET:
        seats = request.GET['seats']
        if seats:
            search = search.filter(seats = seats)    

    if 'Price' in request.GET:
        Price = request.GET['Price']
        if Price:
            search = search.filter(Price = Price)    

    if 'From_index' in request.GET:
        from_date = request.GET['From_index']
        if from_date:
            search = search.filter( from_date =  from_date)  
    if 'to_index' in request.GET:
        to_date = request.GET['to_date']    
        if to_date:
             search = search.filter( to_date =  to_date) 
              
    trip_ = {
        'trips': search 
    }

    return render(request,'Trips.html',trip_ )

def demoAbout(request):
    return render(request,'about us.html')

def demoIn(request):
    
    if request.method == 'POST':
        global email_in 
        email_in = request.POST.get('username')
        password_in = request.POST.get('password')

        print(email_in, password_in)

        emails = User.objects.all()
        for x in emails:
            if x.username == email_in and x.password == password_in:
                global prof_signin_name , prof_signin_pass ,prof_loc , prof_email
                prof_signin_name  = email_in
                prof_signin_pass  = password_in
                prof_loc = x.location
                prof_email = x.email
                return redirect('index')

    
    return render(request,'sign in.html')


def demoUp(request):
    if request.method =='POST':
        user_name = request.POST.get('username')
        user_pass = request.POST.get('password')
        locat = request.POST.get('location')
        email =request.POST.get('email')
        global data
        data = User(username= user_name, password = user_pass, location =locat, email = email)
        data.save()
        return redirect('sign in')
    return render(request,'sign up.html')


def demoStations(request):
    return render(request,'stations.html')

def demoBooked(request):
   
    check = User.objects.get(username = email_in)
    if check.my_trips != None:

        context ={
            'bookedtrip':trip_id,
            'bookednum_seats': num_seats,
            'visa':visa,
        }
        return render(request,'bookedtrips.html',context)

    else:
        
        context ={
            'bookedtrip':None,
            'bookednum_seats': None,
            'visa':None,

        }

        return render(request,'bookedtrips.html',context)


def demoDetails(request):
    total = num_seats * trip_id.Price
    trip_id.Price =total
    Context ={
        'details': trip_id,
        'numSeats': num_seats,
        'visa': visa,
    }
    return render(request,'details.html', Context)

def demoupdate(request):
   
    current_user = User.objects.get(username = email_in)
    
    if request.method == 'POST':
        
        upd_name = request.POST.get('updname')
        upd_email = request.POST.get('updmail')
        upd_pass = request.POST.get('updpass')
        upd_loc = request.POST.get('updaddr')
        current_user.username = upd_name
        current_user.password = upd_pass
        current_user.email = upd_email
        current_user.location = upd_loc
        current_user.save()
    context={
        'form':current_user
    }

        
    return render(request, 'update.html', context)

def demodelete(request):
    user_dele =  User.objects.get(username = email_in)

    if request.method == 'POST':
        
        
        trip_id.seats = trip_id.seats + num_seats
        
        print(trip_id.seats)
        trip_id.save()
        user_dele.my_trips = None
        user_dele.save()
        return redirect('index') 
        

    return render(request, 'delete.html')    