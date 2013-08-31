# Create your views here.
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from models import *


def zapisz(request):
    kurs = Kurs.objects.get(pk=request.POST['kurs_id'])
    if kurs and kurs.wolne() > 0:
        wypisz(request)
        request.user.kurs_set.add(kurs)
        request.user.save()
    return redirect('/kursy')


def wypisz(request):
    kursy = Kurs.objects.get(pk=request.POST['kurs_id']).termin.kurs_set.all()
    for k in kursy:
        request.user.kurs_set.remove(k)
    request.user.save()
    return redirect('/kursy')


def index(request):
    if request.method == 'POST':
        if 'action' in request.POST and\
           'kurs_id' in request.POST:
            if request.POST['action'] == 'wypisz':
                return wypisz(request)
            elif request.POST['action'] == 'zapisz':
                return zapisz(request)
            else:
                return redirect('/kursy')
        else:
            return redirect('/kursy')
    else:
        return render_to_response('kursy_index.html', {'terminy': Termin.objects.all(), }, context_instance=RequestContext(request))
