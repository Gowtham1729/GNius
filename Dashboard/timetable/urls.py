from django.conf.urls import url
from . import views

app_name = 'timetable'

urlpatterns = [
    url(r'^$', views.timetable, name='table'),
    url(r'^events/$', views.events, name='events')

]