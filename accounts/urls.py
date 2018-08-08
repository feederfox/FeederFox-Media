
from django.conf.urls import url,include
from .views import signup,publisher_list,customer_list,advertiser_list,post
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^signup/', signup, name='signup'), 
    url(r'^login/$', auth_views.login, {'template_name': 'account/login.html'} ,name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/accounts/login/'}, name="logout"),
    url(r'^publisher_list/',publisher_list,name='publisher_list'),
    url(r'^customer_list/',customer_list,name='customer_list'),    
    url(r'^advertiser_list/',advertiser_list,name='advertiser_list'),
    url(r'^post/',post,name='post'),
]

