# coding=utf-8
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User 
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.core.validators import email_re
from phonenumber_field.phonenumber import PhoneNumber, to_python
from device.models import UsrExd

@csrf_protect
def change_user( request ):
    '''
    change the information if the user
    '''
    check = check_user( request )
    if check:
        return check
    user = User.objects.get( username__exact = request.user.username )
    psw = request.POST[ 'password' ]
    re_psw = request.POST[ 're_paw' ]
    email = request.POST[ 'email' ]
    phone = to_python( request.POST[ 'phone' ] )
    description = request.POST[ 'description' ]

    error = ''
    if ( len(psw) > 0  ) and ( cmp( psw, re_psw ) == 0 ):
        user.set_password( psw )
    if cmp( psw, re_psw ) != 0:
        error = u'两次密码输入不一致'
    if len(email) != 0 and email_re.match( email ):
        user.email = email
    else:
        error = u'请输入正确的邮箱'
    if not  phone.is_valid():
        error = u'请输入正确的电话号码（例如+8613012345678）'
    else:
        user.usrexd.phone_number = phone

    user.usrexd.description = description

    user.save()
    if not error:
        error = u'成功修改个人信息'

    return render_to_response( 'person.html', {
        'username':user.username,
        'email':user.email,
        'user':request.user,
        'phone':user.usrexd.phone_number,
        'description':user.usrexd.description,
        'error':error
        }, context_instance=RequestContext(request) );

@csrf_protect
def check_user( request ):
    '''
    check whether the user is authenticated.
    return None if is authenticated, else return the response which redirect to login page
    '''
    if not request.user.is_authenticated():
        return redirect( '/login/' )
    else:
        return None

@csrf_protect
def add_user(request):
    '''
    register a user
    '''
    uname = request.POST[ 'username' ]
    email = request.POST[ 'email' ]
    psw = request.POST[ 'password' ]
    re_psw = request.POST[ 're_paw' ]
    phone = to_python( request.POST[ 'phone' ] )
    description = request.POST[ 'description' ]
    

    error = ''
    if len(uname) == 0:
        error = u'请输入用户名'
    elif len( email ) == 0 or not is_valid_email( email ):
        error = u'请输入正确的邮箱'
    elif cmp( psw, re_psw ) != 0:
        error = u'两次密码输入不一致'
    elif not  phone.is_valid():
        error = u'请输入正确的电话号码（例如+8613012345678）'
    else:
        user = User.objects.create_user( uname, email, psw )
        usr_exd = UsrExd( user=user, phone_number=phone, description=description )
        usr_exd.save()
        error = u'注册成功'

    return render_to_response( 'person.html', {
        'username':uname,
        'email':email,
        'phone':str(phone),
        'description':description,
        'user':request.user,
        'error':error
        }, context_instance=RequestContext(request) );

def is_valid_email(email):
    '''
    check is the email valid
    '''
    if email_re.match(email):
        return True
    return False

@csrf_protect
def per_info( request ):
    '''
    display the person infomation
    '''
    check = check_user(request)
    if check:
        return check
    user = User.objects.get( username__exact = request.user.username )
    phone = user.usrexd.phone_number
    description = user.usrexd.description
    if check:
        return check

    return render_to_response( 'person.html', {
            'username':request.user.username,
            'email':request.user.email,
            'phone':str(phone),
            'user':request.user,
            'description':description
        }, context_instance=RequestContext(request) )
    
