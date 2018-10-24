from django.conf.urls import url,include
from .views import postopenings,viewopenings,application

urlpatterns = [
    url(r'^postopenings/', postopenings,name='postopenings'),
    url(r'^viewopenings/',viewopenings,name='viewopenings'),
    url(r'^(?P<pk>[\-\w]+)/application/',application,name='application'),
    ]