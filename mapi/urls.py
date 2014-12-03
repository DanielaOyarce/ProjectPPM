from django.conf.urls import *
from mapi.views import form_mapi

urlpatterns = patterns('',
   url(r'^$', form_mapi),
)
