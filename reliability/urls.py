from django.conf.urls import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  #  url(r'^$', include('aircraft.urls')),
  #  url(r'^reliability/aircraft', include('aircraft.urls')),
    url(r'^$', include('mapi.urls')),
    url(r'^reliability/mapi', include('mapi.urls')),
    url(r'^reliability/admin/', include(admin.site.urls)),
)