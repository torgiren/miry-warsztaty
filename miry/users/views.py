from django.shortcuts import render_to_response, redirect
from django.contrib.auth.models import User
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from models import *


def user_index(request):
    return render_to_response('user_index.html', context_instance=RequestContext(request))


def user_login(request):
    if request.method == 'POST':
        if 'email' in request.POST:
            try:
                u = User.objects.get(email=request.POST['email'])
                u.backend = 'django.contrib.auth.backends.ModelBackend'
                login(request, u)
            except(User.DoesNotExist):
                return redirect('/aaa')
            return redirect('/')
    else:
        return render_to_response('user_login.html', context_instance=RequestContext(request))


def user_logout(request):
    logout(request)
    return redirect('/')

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

def user_preferencje(request):
    if request.method == 'POST':
        if 'preferencje' in request.POST:
            pref = request.user.mieszkanie_set.all()
            if len(pref):
                pref = pref[0]
            else:
                pref = mieszkanie()
                pref.user = request.user
            pref.preferencje = request.POST['preferencje']
            pref.save()
            if len(request.POST['preferencje']) == 0:
                pref.delete()
            return redirect('/')

    return redirect('/')

def user_preferencje_lista(request):
    pref = mieszkanie.objects.all()
    return render_to_response('pref_list.html', {'pref': pref}, context_instance=RequestContext(request))
