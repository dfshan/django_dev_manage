# coding=utf-8
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext

@csrf_protect
def change_user( request ):
    user = User.objects.get( username__exact = request.user.username )
    psw = request.POST[ 'password' ]
    re_psw = request.POST[ 're_paw' ]
    email = request.POST[ 'email' ]
    error = ''
    if ( len(psw) > 0  ) and ( cmp( psw, re_psw ) == 0 ):
        user.set_password( psw )
    if cmp( psw, re_psw ) != 0:
        error = u'两次密码输入不一致'
    if len(email) > 0:
        user.email = email
    user.save()

    return render_to_response( 'person.html', {
        'username':user.username,
        'email':user.email,
        'user':request.user,
        'error':error
        }, context_instance=RequestContext(request) );
