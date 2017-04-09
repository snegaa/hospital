from django.shortcuts import render
from django.http import HttpResponse
from .models import Vrach
# Create your views here.


def hell(request):
    print(request.POST)
    print(request.GET)
    all_vrach = Vrach.objects.all()

    return HttpResponse(render(request, 'main.html',  {'flag':True, 'all_vrach': all_vrach}))