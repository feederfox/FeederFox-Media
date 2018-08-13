from django.conf.urls import url,include
from .views import ebook_list,magazine_list,socialchannels_list

urlpatterns = [
    url(r'^ebook_list/', ebook_list, name='ebook_list'),
    url(r'^magazine_list/',magazine_list,name='magazine_list'),
    url(r'^socialchannels_list',socialchannels_list,name='socialchannels_list'),
    ]