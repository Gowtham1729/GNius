from django.conf.urls import url
from django.contrib import admin
from . import views

app_name='rooms'

urlpatterns=[
    url(r'^$',views.HomeView,name='home'),
    url(r'^requestroom$',views.RequestView,name='requestroom'),
    url(r'^viewrequest$',views.ShowView,name='showrequest'),
    url(r'^detail$', views.DetailView, name='detail'),


  ]