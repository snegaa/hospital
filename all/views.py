from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def hell(request):
    print(request.POST)
    print(request.GET)
    name = 'Masha'
    aaa = 5
    x = 10

    return HttpResponse(render(request, 'main.html',  locals()))