from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Vrach
from avtoriz.forms import AuthForm
from avtoriz.views import proverka
from django.contrib.auth.models import AnonymousUser
from django.contrib import auth
# Create your views here.


def hell(request):
    all_vrach = Vrach.objects.all()
    is_loged = True
    form = AuthForm()
    print(request.user)
    if request.user is None or isinstance(request.user, AnonymousUser):
        print(123)
        is_loged = False
        if request.method.upper() == 'POST':
            form = AuthForm(request.POST)
            if proverka(request, form):
                return redirect('/lk/')

    return HttpResponse(render(request, 'main.html',  {
        'all_vrach': all_vrach,
        'form': form,
        'is_loged': is_loged,
        'user': request.user
    }))


def LK_klient(request):
    if request.user is None or isinstance(request.user, AnonymousUser):
        return redirect('/')
    return HttpResponse(render(request, 'LK_klient.html', ))


def logout(request):
    auth.logout(request)
    return redirect('/')


def zapis(request):
    return HttpResponse(render(request, 'zapis.html'))