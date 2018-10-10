from django.conf.urls import url,include
from .views import payment_process,payment_done,payment_canceled

urlpatterns = [
	url(r'^process/',payment_process,name='process'),
	url(r'^done/',payment_done,name='done'),
	url(r'^canceled/',payment_canceled,name='canceled'),
]