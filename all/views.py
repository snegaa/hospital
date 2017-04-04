from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def hell(request):
    print(request.POST)
    print(request.GET)

    return HttpResponse(render(request, 'main.html',  {'flag':True}))