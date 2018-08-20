from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.models import Profile
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated,AllowAny
from .models import Ebook,Magazine,SocialChannel,RegionalNewsChannel,NationalNewsChannel,NationalNewsPaper,RegionalNewsPaper,Article
from .serializers import (EbookSerializer,MagazineSerializer,SocialChannelSerializer,
							NationalNewsChannelSerializer,RegionalNewsChannelSerializer,NationalNewsPaperSerializer,
							RegionalNewsPaperSerializer,ArticleSerializer,SignupSerializer,UserSerializer)


@api_view(['GET', 'POST'])
def ebook_list(request):
    if request.method == 'GET':
        ebook = Ebook.objects.all()
        serializer = EbookSerializer(ebook, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = EbookSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def magazine_list(request):
    if request.method == 'GET':
        magazine = Magazine.objects.all()
        serializer = MagazineSerializer(magazine, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MagazineSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def socialchannels_list(request):
    if request.method == 'GET':
        socialchannel = SocialChannel.objects.all()
        serializer = SocialChannelSerializer(socialchannel, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SocialChannelSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def nationalchannels_list(request):
    if request.method == 'GET':
        nationalchannel = NationalNewsChannel.objects.all()
        serializer = NationalNewsChannelSerializer(nationalchannel, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = NationalNewsChannelSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def regionalchannels_list(request):
    if request.method == 'GET':
        regionalchannel = RegionalNewsChannel.objects.all()
        serializer = RegionalNewsChannelSerializer(regionalchannel, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RegionalNewsChannelSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def contents_list(request):
	if request.method == 'GET':
		context = {
			"request":request
			}
		ebook = Ebook.objects.all()
		National = NationalNewsChannel.objects.all()
		Regional = RegionalNewsChannel.objects.all()
		magazine = Magazine.objects.all()
		socialchannel = SocialChannel.objects.all()
		national = NationalNewsPaper.objects.all()
		regional = RegionalNewsPaper.objects.all()
		article = Article.objects.all()
		ebookserializer = EbookSerializer(ebook, many=True,context=context)
		magazineserializer = MagazineSerializer(magazine,many=True,context=context)
		socialserializer = SocialChannelSerializer(socialchannel,many=True,context=context)
		NationalSerializer = NationalNewsChannelSerializer(National,many=True,context=context)
		RegionalSerializer = RegionalNewsChannelSerializer(Regional,many=True,context=context)
		nationalserializer = NationalNewsPaperSerializer(national,many=True,context=context)
		regionalserializer = RegionalNewsPaperSerializer(regional,many=True,context=context)
		articleserializer = ArticleSerializer(article,many=True,context=context)
		resp = ebookserializer.data
		resp1 = magazineserializer.data
		resp2 = socialserializer.data
		resp3 = NationalSerializer.data
		resp4 = RegionalSerializer.data
		resp5 = nationalserializer.data
		resp6 = regionalserializer.data
		resp7 = articleserializer.data
		ebk = {'E-Books':resp}
		magaz = {'Magazines':resp1}
		social = {'SocialChannels':resp2}
		national = {'NationalNewsChannels':resp3}
		regional = {'RegionalNewsChannels':resp4}
		nat = {'NationalNewsPapers':resp5}
		reg = {'RegionalNewsPapers':resp6}
		art = {'Articles':resp7}
		b = regional.copy()
		b.update(national)
		news = {'NewsChannels':b}
		c = reg.copy()
		c.update(nat)
		paper = {'NewsPapers':c}
		a = ebk.copy()
		a.update(magaz)
		a.update(social)
		a.update(news)
		a.update(paper)
		a.update(art)
		return Response(a)

    # elif request.method == 'POST':
    #     serializer = RegionalNewsChannelSerializer(data=request.DATA)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(
    #             serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def news(request):
	National = NationalNewsChannel.objects.all()
	Regional = RegionalNewsChannel.objects.all()
	context = {
		'request':request
	}
	NationalSerializer = NationalNewsChannelSerializer(National,many=True,context=context)
	RegionalSerializer = RegionalNewsChannelSerializer(Regional,many=True,context=context)
	response = NationalSerializer.data
	response1 = RegionalSerializer.data
	national = {'NationalNewsChannels':response}
	regional = {'RegionalNewsChannels':response1}
	print(national.items())
	a = national.copy()
	a.update(regional)
	return Response(a)
	


class signup(ListCreateAPIView):
	queryset = Profile.objects.all()
	serializer_class = SignupSerializer

	# def create(self,request,*args,**kwargs):
	# 	serializer = SignupSerializer(data=request.data)
	# 	if serializer.is_valid():
	# 		serializer.save()
	# def create(self, validated_data):
	# 	user = super(SignupSerializer, self).create(validated_data)
	# 	user.set_password(validated_data['password1'])
	# 	user.save()
	# 	return user     