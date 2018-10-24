from django.conf.urls import url,include
from .views import createad,load_edition,addbanner,viewbanner,approvebanner

urlpatterns = [
	url(r'^createad/',createad,name='createad'),
	url(r'^ajax/load-edition/',load_edition,name='ajax-load_edition'),
	url(r'^addbanner/',addbanner,name='addbanner'),
	url(r'^viewbanner/',viewbanner,name='viewbanner'),
	url(r'^(?P<pk>[\-\w]+)/approvebanner/',approvebanner,name='approvebanner'),
]