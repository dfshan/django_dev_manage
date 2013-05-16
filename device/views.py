# Create your views here.
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from device.models import Device, OrderTime
from django_dev_manage.views import check_user

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

def ord_dev_page(request):
    check = check_user( request )
    if check:
        return check
    if 'id' in request.GET:
        dev = Device.objects.get( id = request.GET['id'] )
        return render_to_response( 'ord_dev.html', {
                    'dev': dev,
                    'user': request.user
            })
    else:
        return get_device(request)
