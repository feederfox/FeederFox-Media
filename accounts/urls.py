
from django.conf.urls import url,include
from .views import (signup,publisher_list,customer_list,advertiser_list,post,add_publishers,edit_publishers,add_customers,customer_signup,
    advertiser_signup,edit_customers,add_advertisers,edit_advertisers,delete_publisher,delete_customer,delete_advertiser,publisher_signup)
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^signup/', signup, name='signup'), 
    url(r'^publishersignup/',publisher_signup,name='pubsignup'),
    url(r'^advertisersignup/',publisher_signup,name='advsignup'),
    url(r'^customersignup/',publisher_signup,name='cussignup'),
    url(r'^login/$', auth_views.login, {'template_name': 'account/login.html'} ,name='login'),
    url(r'^adminlogin/',auth_views.login, {'template_name': 'account/admin_login.html'},name='admin_login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name="logout"),
    url(r'^publisher_list/',publisher_list,name='publisher_list'),
    url(r'^add_publishers/',add_publishers,name='add_publishers'),
    url(r'^(?P<pk>[\-\w]+)/edit_publishers/',edit_publishers,name='edit_publishers'),
    url(r'^(?P<pk>[\-\w]+)/delete_publisher/',delete_publisher,name='delete_publisher'),
    url(r'^customer_list/',customer_list,name='customer_list'),    
    url(r'^add_customers/',add_customers,name='add_customers'),
    url(r'^(?P<pk>[\-\w]+)/edit_customers/',edit_customers,name='edit_customers'),
    url(r'^(?P<pk>[\-\w]+)/delete_customer/',delete_customer,name='delete_customer'),
    url(r'^advertiser_list/',advertiser_list,name='advertiser_list'),
    url(r'^add_advertisers/',add_advertisers,name='add_advertisers'),
    url(r'^(?P<pk>[\-\w]+)/edit_advertisers/',edit_advertisers,name='edit_advertisers'),
    url(r'^(?P<pk>[\-\w]+)/delete_advertiser/',delete_advertiser,name='delete_advertiser'),
    url(r'^post/',post,name='post'),
]

