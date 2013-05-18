# coding=utf-8
# Create your views here.
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from device.models import Device, OrderTime, User as User
from django.contrib.auth.models import User as User2
from django_dev_manage.views import check_user
from datetime import datetime

@csrf_protect
def get_device(request):
    check = check_user( request )
    if check:
        return check
    devices = Device.objects.all()
    return render_to_response( 'inq_dev.html', {
        'devices': devices,
        'user': request.user
        }, context_instance=RequestContext(request) )

@csrf_protect
def ord_dev_page(request):
    check = check_user( request )
    if check:
        return check
    if 'id' in request.GET:
        dev = Device.objects.get( id = request.GET['id'] )
        return render_to_response( 'ord_dev.html', {
                    'dev': dev,
                    'user': request.user
        }, context_instance=RequestContext(request) )

    else:
        return get_device(request)

@csrf_protect
def ord_device(request):
    check = check_user(request)
    if check:
        return check
    st_time = request.POST[ 'st_time' ]
    st_time = datetime.strptime( st_time, '%Y-%m-%d %H:%M:%S' )
    ed_time = request.POST[ 'ed_time' ]
    ed_time = datetime.strptime( ed_time, '%Y-%m-%d %H:%M:%S' )
    dev = Device.objects.get( id = int(request.POST['id'] ) )

    user = User2.objects.get( username=request.user.username )

    user = User.objects.get( user = user )
    ord_time = OrderTime.objects.filter( dev=dev )
    error = ''
    if st_time >= ed_time or st_time < datetime.now():
        error='请输入一个正确的时间！'
        return render_to_response( 'ord_dev.html', {
                'error':error,
                'dev': dev,
                'user': request.user
            }, context_instance=RequestContext(request))
    
    for time in ord_time:
        if ( time.startTime <= st_time < time.endTime ) or ( time.startTime < ed_time <= time.edTime ):
            error = "当前时间段，设备已经被预定，请选择其它时间！"
            return render_to_response( 'ord_dev.html', {
                    'error':error,
                    'dev': dev,
                    'user': request.user
            }, context_instance=RequestContext(request))
    OrderTime( startTime=st_time, endTime = ed_time, user = user, dev=dev ).save()
    error = '预约成功'
    return render_to_response( 'ord_dev.html', {
                'error':error,
                'dev': dev,
                'user': request.user
            }, context_instance=RequestContext(request))
    

