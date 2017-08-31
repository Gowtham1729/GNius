from django.conf.urls import url
from django.contrib import admin
from . import views

app_name='lostfound'

urlpatterns=[
    url(r'^$',views.HomeView,name='homelost'),
    url(r'^reportlost$',views.LostView,name='reportlost'),
    url(r'^reportfound$',views.FoundView,name='reportfound'),
    url(r'^matchfound$',views.CompareView,name='matchfound'),
 ]