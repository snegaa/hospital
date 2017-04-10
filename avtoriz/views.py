from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def proverka(request, form):
    print('A'*20, form)
    if form.is_valid():
        _username = form.cleaned_data['login']
        _password = form.cleaned_data['password']
        user = authenticate(username=_username, password=_password)
        if user is not None:
            login(request, user)
            return True
        return False
