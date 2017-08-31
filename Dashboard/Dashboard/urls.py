from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^mess/', include('mess.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^terashare/', include('terashare.urls')),
    url(r'', include('profiles.urls')),
    url(r'^timetable/', include('timetable.urls')),
    url(r'^parcel/', include('parcels.urls')),
    url(r'^shuttle/', include('shuttleservice.urls')),
    url(r'^welfare/', include('welfare.urls')),
    url(r'^rooms/', include('rooms.urls')),
    url(r'^', include('home.urls')),
    url(r'^lostfound/',include('lostfound.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)