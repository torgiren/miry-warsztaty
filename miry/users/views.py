from django.shortcuts import render_to_response, redirect
from django.contrib.auth.models import User
from django.template import RequestContext


def index(request):
    return render_to_response('user_index.html')


def login(request):
    return render_to_response('user_login.html')


def logout(request):
    return render_to_response('user_logout.html')


def register(request):
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
                    return redirect('/kursy')
    else:
        return render_to_response('user_register.html', context_instance=RequestContext(request))
