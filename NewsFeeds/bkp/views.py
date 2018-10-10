from django.shortcuts import render
from .models import NewsFeed
from .forms import NewsFeedsForm
from django.contrib import messages
from .serializers import NewsFeedSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


def addnewsfeeds(request):
	if request.method =='POST':
		form = NewsFeedsForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request,'Successfully Uploaded')
	form = NewsFeedsForm()
	return render(request,'addnewsfeeds.html',{'form':form})		

def viewtotalnewsfeeds(request):
	newsfeeds = NewsFeed.objects.all()
	return render(request,'viewtotalnewsfeeds.html',{'newsfeeds':newsfeeds})


def headlinenewsfeed(request):
	newsfeeds = NewsFeed.objects.filter(category = '1')
	category = 'Headlines/Breaking News'
	return render(request,'newsfeeds.html',{'newsfeeds':newsfeeds,'category':category})


def educationnewsfeed(request):
	newsfeeds = NewsFeed.objects.filter(category = '2')
	print(newsfeeds)
	category = 'Education'
	return render(request,'newsfeeds.html',{'newsfeeds':newsfeeds,'category':category})

def entertainmentnewsfeed(request):
	newsfeeds = NewsFeed.objects.filter(category = '3')
	category = 'Entertainment'
	return render(request,'newsfeeds.html',{'newsfeeds':newsfeeds,'category':category})


def businessnewsfeed(request):
	newsfeeds = NewsFeed.objects.filter(category = '4')
	category = 'Business'
	return render(request,'newsfeeds.html',{'newsfeeds':newsfeeds,'category':category})

def sportsnewsfeed(request):
	newsfeeds = NewsFeed.objects.filter(category = '5')
	category = 'Sports'
	return render(request,'newsfeeds.html',{'newsfeeds':newsfeeds,'category':category})


def lifestylenewsfeed(request):
	newsfeeds = NewsFeed.objects.filter(category = '6')
	print(newsfeeds)
	category = 'Life Style'
	return render(request,'newsfeeds.html',{'newsfeeds':newsfeeds,'category':category})

def socialnewsfeed(request):
	newsfeeds = NewsFeed.objects.filter(category = '7')
	category = 'Social'
	return render(request,'newsfeeds.html',{'newsfeeds':newsfeeds,'category':category})


def internationalnewsfeed(request):
	newsfeeds = NewsFeed.objects.filter(category = '8')
	category = 'World/International'
	return render(request,'newsfeeds.html',{'newsfeeds':newsfeeds,'category':category})

def globalnewsfeed(request):
	newsfeeds = NewsFeed.objects.filter(category = '9')
	category = 'Global'
	return render(request,'newsfeeds.html',{'newsfeeds':newsfeeds,'category':category})

@api_view(['GET','POST'])
def newsfeedsapi(request):
    context = {
            "request":request
            }
    newsfeed = NewsFeed.objects.all()
    newsfeedserializer = NewsFeedSerializer(newsfeed,many=True,context=context)
    resp3 = newsfeedserializer.data
    a = {'NewsFeeds':resp3}
    return Response(a)	