from django.conf.urls import url,include
from .views import (ebook_list,magazine_list,socialchannels_list,news,nationalchannels_list,regionalchannels_list,
contents_list,signup,regionalpapers_list,nationalpapers_list,Articles,android,login,newspapers_list)

urlpatterns = [
    url(r'^ebook_list/', ebook_list, name='ebook_list'),
    url(r'^magazine_list/',magazine_list,name='magazine_list'),
    url(r'^socialchannels_list',socialchannels_list,name='socialchannels_list'),
    url(r'^newschannels',news,name='newschannels'),
    url(r'^nationalchannels_list/',nationalchannels_list,name='nationalchannels_list'),
    url(r'^regionalchannels_list/',regionalchannels_list,name='regionalchannels_list'),
    url(r'^nationalpapers_list/',newspapers_list,name='nationalpapers_list'),
    url(r'^regionalpapers_list/',regionalpapers_list,name='regionalpapers_list'),
    url(r'^contents/',contents_list,name='contents_list'),
    url(r'^signup/',signup.as_view(),name='signup'),
    url(r'^articles/',Articles,name='articles'),

    url(r'^login/',login.as_view(),name='login'),
    url(r'^articles/',Articles,name='articles'),
    url(r'^android/',android,name='android'),
    #url(r'^create/',create_user,name='create_user'),
    ]