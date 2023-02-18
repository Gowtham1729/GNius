from django.conf.urls import url
from . import views

app_name = 'welfare'

urlpatterns = [
    url(r'^home/$', views.Home, name='home'),
    url(r'^complain/$', views.complaint, name='register'),
    url(r'^complaints/$', views.complaints, name='complaints')
]