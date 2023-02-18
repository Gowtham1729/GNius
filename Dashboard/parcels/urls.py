from django.conf.urls import url
from . import views

app_name = 'parcel'


urlpatterns = [
    url(r'^$', views.homepage, name='parcels')
]