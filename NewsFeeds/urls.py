from django.conf.urls import url,include
from .views import (newsfeed, shownewsfeed, sports,educational,headlines,globalss,world,social,
    business,lifestyle,entertainment,newsfeeddescription,NewsapiViewSet,newsfeedsdetail)

urlpatterns = [
    url(r'^newsfeed/',newsfeed,name='newsfeed'),
    url(r'^shownewsfeed/',shownewsfeed,name='shownewsfeed'),
    url(r'^sports/',sports,name='sports'),
    url(r'^educational/',educational,name='educational'),
    url(r'^headlines/',headlines,name='headlines'),
    url(r'^globalss/',globalss,name='globalss'),
    url(r'^world/',world,name='world'),
    url(r'^social/',social,name='social'),
    url(r'^entertainment/',entertainment,name='entertainment'),
    url(r'^business/',business,name='business'),
    url(r'^lifestyle/',lifestyle,name='lifestyle'),
    url(r'^(?P<pk>[\-\w]+)/newsfeeddescription/',newsfeeddescription,name='newsfeeddescription'),
    url(r'^newsapi/',NewsapiViewSet.as_view({'get':'list'}),name='newsapi'),
    url(r'^(?P<pk>[\-\w]+)/newsfeedsdetail/',newsfeedsdetail,name='newsfeedsdetail'),
    ]