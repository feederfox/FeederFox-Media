from django.conf.urls import url,include
from .views import ebook_list,magazine_list,socialchannels_list,news,nationalchannels_list,regionalchannels_list,contents_list,signup

urlpatterns = [
    url(r'^ebook_list/', ebook_list, name='ebook_list'),
    url(r'^magazine_list/',magazine_list,name='magazine_list'),
    url(r'^socialchannels_list',socialchannels_list,name='socialchannels_list'),
    url(r'^newschannels',news,name='newschannels'),
    url(r'^nn/',nationalchannels_list,name='nationalchannels_list'),
    url(r'^rn/',regionalchannels_list,name='regionalchannels_list'),
    url(r'^contents/',contents_list,name='contents_list'),
    url(r'^signup/',signup.as_view(),name='signup'),
    #url(r'^create/',create_user,name='create_user'),
    ]