from django.conf.urls import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'reliability.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('aircraft.urls')),
    url(r'^reliability/aircraft', include('aircraft.urls')),
    url(r'^reliability/admin/', include(admin.site.urls)),
   
)
