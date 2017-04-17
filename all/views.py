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
    if request.user is None or isinstance(request.user, AnonymousUser):
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
    return HttpResponse(render(request, 'LK_klient.html', {
        'is_loged': True,
        'user': request.user
    }))


def logout(request):
    auth.logout(request)
    return redirect('/')


def zapis(request):
    if request.user is None or isinstance(request.user, AnonymousUser):
        return redirect('/')
    return HttpResponse(render(request, 'zapis.html' , {
        'is_loged': True,
        'user': request.user
    }))


def logout(request):
    auth.logout(request)
    return redirect('/')


def vyzovyNaDom(request):
    if request.user is None or isinstance(request.user, AnonymousUser):
        return redirect('/')
    return HttpResponse(render(request, 'vyzovy_na_dom.html', {
        'is_loged': True,
        'user': request.user
    }))


def logout(request):
    auth.logout(request)
    return redirect('/')


def future_visits(request):
    if request.user is None or isinstance(request.user, AnonymousUser):
        return redirect('/')
    return HttpResponse(render(request, 'future_visits.html', {
        'is_loged': True,
        'user': request.user
    }))


def logout(request):
    auth.logout(request)
    return redirect('/')


def past_visits(request):
    if request.user is None or isinstance(request.user, AnonymousUser):
        return redirect('/')
    return HttpResponse(render(request, 'past_visits.html', {
        'is_loged': True,
        'user': request.user
    }))


def logout(request):
    auth.logout(request)
    return redirect('/')


def helpful_information(request):
    if request.user is None or isinstance(request.user, AnonymousUser):
        return redirect('/')
    return HttpResponse(render(request, 'helpful_information.html', {
        'is_loged': True,
        'user': request.user
    }))


def LK_Vrach(request):
    if request.user is None or isinstance(request.user, AnonymousUser):
        return redirect('/')
    return HttpResponse(render(request, 'lk_Vrach.html', {
        'is_loged': True,
        'user': request.user
    }))


def logout(request):
    auth.logout(request)
    return redirect('/')

