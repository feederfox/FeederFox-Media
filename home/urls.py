
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
    url(r'^video1/',views.video1,name='video1'),
    url(r'^video2/',views.video2,name='video2'),
    url(r'^video3/',views.video3,name='video3'),
    url(r'^video4/',views.video4,name='video4'),
    url(r'^video5/',views.video5,name='video5'),
    url(r'^video6/',views.video6,name='video6'),
    url(r'^video7/',views.video7,name='video7'),
    url(r'^publisherpage/',views.publisherpage,name='publisherpage'),
    url(r'^customerpage/',views.customerpage,name='customerpage'),
    url(r'^advertiserpage/',views.advertiserpage,name='advertiserpage'),


]