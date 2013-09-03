# Create your views here.
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from models import *


def zapisz(request):
    kurs = Kurs.objects.get(pk=request.POST['kurs_id'])
    if kurs and kurs.wolne() > 0:
        wypisz(request)
        request.user.kurs_set.add(kurs)
        request.user.save()
    return redirect('/')


def wypisz(request):
    kursy = Kurs.objects.get(pk=request.POST['kurs_id']).termin.kurs_set.all()
    for k in kursy:
        request.user.kurs_set.remove(k)
    request.user.save()
    return redirect('/')



@login_required(login_url='/user/login')
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
        pref = request.user.mieszkanie_set.all()
        if len(pref):
            pref = pref[0].preferencje
        else:
            pref = ""
        return render_to_response('kursy_index.html', {'terminy': Termin.objects.all(), 'pref': pref }, context_instance=RequestContext(request))

def lista(request, kurs):
    k = Kurs.objects.get(pk=kurs)
    ludzie = k.osoby.all()
    return render_to_response('kursy_uczestnicy.html', {'ludzie': ludzie, 'k': k}, context_instance=RequestContext(request))
