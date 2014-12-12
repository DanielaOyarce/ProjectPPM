from django.conf.urls import *
from hourscycles.views import form_hourscycles

urlpatterns = patterns('',
   url(r'^$', form_hourscycles),
)
