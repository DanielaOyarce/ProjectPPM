from django.conf.urls import *
from hourscycles.views import UploadHoursCyclesView, HomeView, ReportView, utilization, graphics_utilization

urlpatterns = patterns('',
	url(r'^$', HomeView.as_view(), name='index'),
	url(r'^hourscycles/upload/$', UploadHoursCyclesView, name='upload-hourscycles'),
	url(r'^hourscycles/utilization/$', utilization, name='utilization-hourscycles'),
	url(r'^hourscycles/graphics_utilization/$', graphics_utilization, name='graphics_utilization-hourscycles'),
)
