from django.conf.urls import *
from aircraft.views import archives

urlpatterns = patterns('',
   url(r'^$', archives),
)
