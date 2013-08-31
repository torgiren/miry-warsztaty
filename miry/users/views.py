from django.shortcuts import render_to_response, redirect
from django.contrib.auth.models import User
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout


def user_index(request):
    return render_to_response('user_index.html', context_instance=RequestContext(request))


def user_login(request):
    if request.method == 'POST':
       if 'login' in request.POST and\
          'passwd' in request.POST:
            user = authenticate(username=request.POST['login'], password=request.POST['passwd'])
            if user is not None:
                login(request, user)
            return redirect('/user')
    else:
        return render_to_response('user_login.html', context_instance=RequestContext(request))


def user_logout(request):
    logout(request)
    return redirect('/user')

def user_register(request):
    if request.method == 'POST':
        if 'imie' in request.POST and\
           'nazwisko' in request.POST and\
           'login' in request.POST and\
           'passwd' in request.POST and\
           'passwd2' in request.POST and\
           'email' in request.POST:
               if request.POST['passwd'] == request.POST['passwd2']:
                    user = User.objects.create_user(request.POST['login'], request.POST['email'], request.POST['passwd'], first_name=request.POST['imie'], last_name=request.POST['nazwisko'])
                    user.save()
                    return redirect('/user')
    else:
        return render_to_response('user_register.html', context_instance=RequestContext(request))
