# coding=utf-8
from django.contrib import admin, sites
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin
from device.models import Device, UsrExd, OrderTime

class UsrExdInline( admin.StackedInline ):
    model = UsrExd
    can_delete = False
    verbose_name_plural = '其它信息'

class UserAdmin( UserAdmin ):
    inlines = ( UsrExdInline, )

admin.site.register(Device)
admin.site.register(OrderTime)

admin.site.unregister( User )
admin.site.register( User, UserAdmin )
