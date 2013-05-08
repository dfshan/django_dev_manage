# Create your views here.
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext

@csrf_protect
def per_info( request ):
    return render_to_response( 'person.html', {
            'username':request.user.username,
            'email':request.user.email,
            'user':request.user
        }, context_instance=RequestContext(request) )
    
    
