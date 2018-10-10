from django.shortcuts import render
from decimal import Decimal
from django.conf import settings
from django.core.urlresolvers import reverse
from paypal.standard.forms import PayPalPaymentsForm
from contents.models import EbookUpload
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def payment_done(request):
	ebook_id = request.session.get('ebook_id')
	print(ebook_id)
	return render(request,'payment/done.html',{})

@csrf_exempt
def payment_canceled(request):
	return render(request,'payment/canceled.html',{})

def payment_process(request):
	ebook_id = request.session.get('ebook_id')
	ebook = EbookUpload.objects.get(id = ebook_id)
	pdf = ebook.pdf
	name = ebook.name
	author = ebook.author
	host = request.get_host()

	paypal_dict = {
		'business':settings.PAYPAL_RECEIVER_EMAIL,
		'amount': 100,
		'item_name': 'Ebook {}'.format(ebook.name),
		'invoice':str(ebook.id),
		'currency_code':'INR',
		'notify_url':'http://{}{}'.format(host,reverse('paypal-ipn')),
		'return_url':'http://{}{}'.format(host,reverse('payment:done')),
		'cancel_url':'http://{}{}'.format(host,reverse('payment:canceled')),
	}

	form = PayPalPaymentsForm(initial = paypal_dict)
	return render(request,'viewebooks.html',{'pdf':pdf,'name':name,'author':author,'form':form})