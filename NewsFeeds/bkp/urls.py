from django.conf.urls import url, include
from .views import (addnewsfeeds,viewtotalnewsfeeds,educationnewsfeed,headlinenewsfeed,entertainmentnewsfeed,
	businessnewsfeed,sportsnewsfeed,lifestylenewsfeed,socialnewsfeed,internationalnewsfeed,globalnewsfeed,newsfeedsapi)

urlpatterns = [
    url(r'^addnewsfeeds/',addnewsfeeds,name = 'addnewsfeeds'),
    url(r'^viewtotalnewsfeeds/',viewtotalnewsfeeds,name='viewtotalnewsfeeds'),
    url(r'^educationnewsfeed/',educationnewsfeed,name='educationnewsfeed'),
    url(r'^headlinenewsfeed/',headlinenewsfeed,name='headlinenewsfeed'),
    url(r'^entertainmentnewsfeed/',entertainmentnewsfeed,name='entertainmentnewsfeed'),
    url(r'^businessnewsfeed/',businessnewsfeed,name='businessnewsfeed'),
    url(r'^sportsnewsfeed/',sportsnewsfeed,name='sportsnewsfeed'),
    url(r'^lifestylenewsfeed/',lifestylenewsfeed,name='lifestylenewsfeed'),
    url(r'^socialnewsfeed/',socialnewsfeed,name='socialnewsfeed'),
    url(r'^internationalnewsfeed/',internationalnewsfeed,name='internationalnewsfeed'),
    url(r'^globalnewsfeed/',globalnewsfeed,name='globalnewsfeed'),
    url(r'^newsfeedsapi/',newsfeedsapi,name='newsfeedsapi'),
    ]