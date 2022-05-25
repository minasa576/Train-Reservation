
from django.db import models
from django.contrib.auth.models import User
from django.db.models.aggregates import Min
from django.db.models.fields import BLANK_CHOICE_DASH, DateField

# Create your models here.


class Train(models.Model):
     
    train_category = [
        ('Luxurious, Wide,Single Seat', 'Luxurious, Wide,Single Seat'),
        
    ]

    train_type=[
        ('Direct , Non Stop','Direct , Non Stop'),
        
    ]
    train_support =[
        ('Yes',"Yes"),
        ('No','No'),
    ]
    
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    status = models.CharField(max_length=50, choices=train_category, null = True, blank =True)
    type = models.CharField(max_length=50, choices=train_type, null=True, blank=True)
    private_screens = models.CharField(max_length=50 , choices=train_support, null=True, blank=True)
    free_snacks = models.CharField(max_length=50,choices=train_support, null=True, blank=True )
    USB_support = models.CharField(max_length=50, choices=train_support, null=True, blank=True )
    Earphone = models.CharField(max_length=50, choices=train_support, null=True, blank=True )
    WIFi = models.CharField(max_length=50, choices=train_support, null=True, blank=True )
    WC = models.CharField(max_length=50, choices=train_support, null=True, blank=True )
    image = models.ImageField  (upload_to = 'photos', null = True, blank = True)
    

class Trip(models.Model):
    trip_no = models.CharField(max_length=100 ,null=False, blank=False)
    Departure_Time = models.TimeField(null=True, blank = True)
    Arrival_Time =models.TimeField(null=True, blank = True)
    Price = models.IntegerField(null=False)
    Classtrain = models.ForeignKey(Train, on_delete=models.PROTECT, null = True, blank=True)
    from_station  = models.CharField(max_length=100 , null=True , blank=True)
    to_station = models.CharField(max_length=100 , null=True , blank=True)
    from_date = DateField(null=True)
    to_date = DateField(null=True)
    seats = models.IntegerField( null = False)
    def __str__(self):
        return self.trip_no

class User(models.Model):
    username = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=50, null=True)
    location = models.CharField(max_length=80, null=True)
    email =models.EmailField(max_length=200, null=True)
    my_trips= models.ForeignKey(Trip ,on_delete=models.CASCADE, null = True, blank=True )

