from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class User( models.Model ):
    # userId = models.IntegerField( primary_key = True )
    # name = models.CharField( max_length = 20 )
    # email = models.EmailField( blank = True )
    user = models.OneToOneField(User)
    phone_number = PhoneNumberField( blank = True )
    def __unicode__(self):
        return self.user.username
    
class Device( models.Model ):
    name = models.CharField( max_length = 20 )
    price = models.IntegerField()
    costPerHour = models.DecimalField( max_digits = 4, decimal_places = 1 )
    orderTime = models.ManyToManyField( User, through = 'OrderTime' )
    def __unicode__(self):
        return self.name

class OrderTime( models.Model ):
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    user = models.ForeignKey( User )
    dev = models.ForeignKey( Device )
    def __unicode__(self):
        return u"Device %s used by %s from %s to %s" % dev, user, startTime, endTime
