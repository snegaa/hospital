
from django.http.response import HttpResponse
# Create your views here.


def printff(a):
    return HttpResponse('message1')


def aaa(bbb):
    return HttpResponse(r"<form method='post' action='.'><input type='button' value='click'/></form>")
