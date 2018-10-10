from django.shortcuts import render
from .models import Newsfeeds
from .forms import NewsfeedsForm
from .serializers import NewsfeedsSerializers
from rest_framework import viewsets
# Create your views here.
def newsfeed(request):
	if request.method == 'POST':
		news=NewsfeedsForm(request.POST,request.FILES)
		if news.is_valid():
			news.save()
	news=NewsfeedsForm()
	return render(request,"newsfeed.html",{'form':news})  

def shownewsfeed(request):
	display = Newsfeeds.objects.all()
	print(display)
	return render(request,'shownewsfeed.html', {'r':display})



def headlines(request):
	data=Newsfeeds.objects.all()
	print(data)
	h=Newsfeeds.objects.filter(category="Headlines")
	category="Headlines"
	return render(request,'newsfeeds.html', {'r':h,'category':category})

def sports(request):
	data=Newsfeeds.objects.all()
	print(data)
	s=Newsfeeds.objects.filter(category="Sports")
	category="Sports"
	return render(request,'newsfeeds.html', {'r':s,'category':category})

def educational(request):
	data=Newsfeeds.objects.all()
	print(data)
	ed=Newsfeeds.objects.filter(category="Educational")
	category="Educational"
	return render(request,'newsfeeds.html', {'r':ed,'category':category})

def business(request):
	data=Newsfeeds.objects.all()
	print(data)
	b=Newsfeeds.objects.filter(category="Business")
	category="Business"
	return render(request,'newsfeeds.html', {'r':b,'category':category})

def entertainment(request):
	data=Newsfeeds.objects.all()
	print(data)
	en=Newsfeeds.objects.filter(category="Entertainment")
	category="Entertainment"
	return render(request,'newsfeeds.html', {'r':en,'category':category})

def social(request):
	data=Newsfeeds.objects.all()
	print(data)
	so=Newsfeeds.objects.filter(category="Social")
	category="Social"
	return render(request,'newsfeeds.html', {'r':so,'category':category})


def globalss(request):
	data=Newsfeeds.objects.all()
	print(data)
	g=Newsfeeds.objects.filter(category="Global")
	category="Global"
	return render(request,'newsfeeds.html', {'r':g,'category':category})


def world(request):
	data=Newsfeeds.objects.all()
	print(data)
	w=Newsfeeds.objects.filter(category="World")
	category="World"
	return render(request,'newsfeeds.html', {'r':w,'category':category})

def lifestyle(request):
	data=Newsfeeds.objects.all()
	print(data)
	l=Newsfeeds.objects.filter(category="Lifestyle")
	category="Lifestyle"
	return render(request,'newsfeeds.html', {'r':l,'category':category})

def newsfeeddescription(request,pk):
	data=Newsfeeds.objects.get(pk=pk)
	print(data)
	return render(request,'newsfeeddescription.html',{'r':data})

# def newsapi(request):
# 	dataapi=Newsfeeds.objects.all()
# 	# a=NewsfeedsSerializers
# 	return render(request,'newsapi.html',{'r':dataapi})

class NewsapiViewSet(viewsets.ModelViewSet):
   
    queryset = Newsfeeds.objects.all()
    serializer_class = NewsfeedsSerializers

def newsfeedsdetail(request,pk):
	data=Newsfeeds.objects.get(pk=pk)
	print(data)
	c=data.category
	alldata=Newsfeeds.objects.filter(category=c).exclude(pk=pk)
	print(alldata)
	return render(request,'newsfeedsdetail.html',{'r':data,'d':alldata})