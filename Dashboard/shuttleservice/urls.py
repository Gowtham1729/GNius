from django.conf.urls import url

from . import views

app_name = 'shuttleservice'

urlpatterns = [
    url(r'^buses/$', views.BusView, name='buses')
]
