# djangotemplates/example/urls.py

from django.conf.urls import url
from home import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'), # Notice the URL has been named
    url(r'^publishersignup/$', views.PublisherSignupPageView.as_view(), name='publisher_signup'),
    url(r'^about/$', views.AboutPageView.as_view(), name='about'),
    url(r'^faq/$', views.FaqPageView.as_view(), name='faq'),
    url(r'^privacy/$', views.PrivacyPageView.as_view(), name='privacy'),
    url(r'^dashboard/$',views.dashboard,name='dashboard'),
    #url(r'^post/',views.post,name='post')
]

