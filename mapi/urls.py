from django.conf.urls import *
from mapi.views import UploadMapiView, HomeView, ReportView

urlpatterns = patterns('',
	url(r'^$', HomeView.as_view(), name='index'),
	url(r'^download/pireps/$', ReportView, name='download-pireps'),
	url(r'^upload/pireps/$', UploadMapiView, name='upload-pireps'),
)