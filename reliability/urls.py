from django.conf.urls import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',    
    url(r'^', include('mapi.urls')),
    url(r'^', include('hourscycles.urls')),
    url(r'^admin/', include(admin.site.urls)),
)