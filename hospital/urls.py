"""hospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include

from django.contrib import admin

from all import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.hell),
    url(r'^lk/', views.LK_klient),
    url(r'^logout/', views.logout),
    url(r'^select_time/(?P<id>[0-9]+)/', views.select_time),
    url(r'^vyzovy_na_dom/', views.vyzovyNaDom),
    url(r'^future_visits/', views.future_visits),
    url(r'^past_visits/', views.past_visits),
    url(r'^helpful_information/', views.helpful_information),
    url(r'^lk_vrach/', views.LK_Vrach),
    url(r'^select_doctor/', views.select_doctor),



]

