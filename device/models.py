# coding=utf-8
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class UsrExd( models.Model ):
    # userId = models.IntegerField( primary_key = True )
    # name = models.CharField( max_length = 20 )
    # email = models.EmailField( blank = True )
    user = models.OneToOneField(User, primary_key = True )
    phone_number = PhoneNumberField( u'联系方式',blank = True )
    description = models.TextField( u'用户描述' )
    def __unicode__(self):
        return self.user.username

    class Meta:
        verbose_name = u"其它用户信息"
        verbose_name_plural = verbose_name
        app_label=u"设备管理"
        db_table='device_usrexd'
    
class Device( models.Model ):
    name = models.CharField( u'设备名称', max_length = 20 )
    price = models.IntegerField( u'设备价格(元)' )
    cost_per_hour = models.DecimalField( u'租借单价(元/小时)', max_digits = 4, decimal_places = 1 )
    order_time = models.ManyToManyField(  User, through = 'OrderTime' )
    description = models.TextField( u'设备描述' )
    buy_date = models.DateField( u'购买时间' )
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u"设备"
        verbose_name_plural = verbose_name
        app_label=u"设备管理"
        db_table='device_device'

class OrderTime( models.Model ):
    start_time = models.DateTimeField( u'开始时间' )
    end_time = models.DateTimeField( u'结束时间' )
    user = models.ForeignKey( User )
    dev = models.ForeignKey( Device )
    def __unicode__(self):
        return u"Device %s used by %s from %s to %s" % ( self.dev, self.user, self.startTime, self.endTime )

    class Meta:
        verbose_name = u"预约时间"
        verbose_name_plural = verbose_name
        app_label=u"设备管理"
        db_table='device_ordertime'
