from django.conf.urls import url
from . import views

app_name = 'terashare'

urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^course/(?P<course_id>[0-9]+)/(?P<folder_id>[0-9]+)/$', views.files, name='files'),
    url(r'^(?P<course_id>[0-9]+)/(?P<folder_id>[0-9]+)/(?P<file_id>[0-9]+)/download/$', views.download, name='download'),
    url(r'^(?P<course_id>[0-9]+)/(?P<folder_id>[0-9]+)/(?P<file_id>[0-9]+)/report/$', views.report, name='report'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^search/$', views.search, name='search_course'),
    url(r'^search/results/$', views.searchres, name='search_results'),

]
