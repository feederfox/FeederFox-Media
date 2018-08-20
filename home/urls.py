# djangotemplates/example/urls.py

from django.conf.urls import url
from home import views

urlpatterns = [
    url(r'^$', views.index, name='home'), # Notice the URL has been named
    url(r'^about/$', views.AboutPageView.as_view(), name='about'),
    url(r'^faq/$', views.FaqPageView.as_view(), name='faq'),
    url(r'^contact/',views.contact,name='contact'),
    url(r'^privacy/$', views.PrivacyPageView.as_view(), name='privacy'),
    url(r'^dashboard/$',views.dashboard,name='dashboard'),
    url(r'^admin/',views.admin,name='admin'),
    url(r'^article1/',views.article1,name='article1'),
    url(r'^article2/',views.article2,name='article2'),
    url(r'^article3/',views.article3,name='article3'),
    url(r'^article4/',views.article4,name='article4'),
    url(r'^regionalnewspaper/',views.regionalnewspaper,name='regionalnewspaper'),

    #url(r'^post/',views.post,name='post')
]