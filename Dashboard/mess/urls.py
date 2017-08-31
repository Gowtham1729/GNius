from django.conf.urls import url
from . import views

app_name = 'mess'

urlpatterns = [
    url(r'^jaiswal/$', views.menu_jaiswal, name='jaiswal'),
]