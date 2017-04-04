from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'a/$', views.printff),
    url(r'dog/$', views.aaa),


]
