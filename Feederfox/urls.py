
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from home import views as core_views
from rest_auth.views import PasswordResetView, PasswordResetConfirmView


urlpatterns = [
    url(r'^ad/', admin.site.urls),
    url(r'^', include('home.urls')),
    url(r'^accounts/',include('accounts.urls',namespace='accounts')),
    url(r'^account/',include('allauth.urls')),
    url(r'^oauth/', include('social_django.urls',namespace='social')),
    url(r'^content/', include('contents.urls',namespace='content')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^auth/',include('django.contrib.auth.urls')),
    url(r'^forgot/', include('django_rest_passwordreset.urls')),
    url(r'^api/login/',include('rest_social_auth.urls_session')),
    url(r'^oauth/', include('social_django.urls',namespace='social')),
    url(r'^settings/$', core_views.settings, name='settings'),
    url(r'^settings/password/$', core_views.password, name='password'),
    url(r'^password/reset/$',PasswordResetView.as_view(),name='password_reset'),
    url(r'^password/reset/confirm/$',PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    url(r'^newsfeeds/',include('NewsFeeds.urls',namespace='newsfeeds')),
    url(r'^paypal/',include('paypal.standard.ipn.urls')),
    url(r'^payment/',include('payments.urls',namespace='payment')),
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings', app_name='ratings')),
    url(r'^careers/',include('careers.urls',namespace='careers')),
    url(r'^advertisement/',include('advertisement.urls',namespace='advertisement')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)