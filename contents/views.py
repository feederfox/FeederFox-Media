from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.models import Profile
from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView,CreateAPIView
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.http import HttpResponse
from django.contrib.auth import authenticate,login

from rest_framework.authtoken.models import Token
from .models import Ebook,Magazine,SocialChannel,RegionalNewsChannel,NationalNewsChannel,NationalNewsPaper,RegionalNewsPaper,Article
from .serializers import (EbookSerializer,MagazineSerializer,SocialChannelSerializer,
							NationalNewsChannelSerializer,RegionalNewsChannelSerializer,NationalNewsPaperSerializer,
							RegionalNewsPaperSerializer,ArticleSerializer,SignupSerializer,LoginSerializer)


# @api_view(['GET', 'POST'])
# def ebook_list(request):
#     if request.method == 'GET':
#         ebook = Ebook.objects.all()
#         serializer = EbookSerializer(ebook, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = EbookSerializer(data=request.DATA)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(
#                 serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'POST'])
# def magazine_list(request):
#     if request.method == 'GET':
#         magazine = Magazine.objects.all()
#         serializer = MagazineSerializer(magazine, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = MagazineSerializer(data=request.DATA)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(
#                 serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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

# @api_view(['GET', 'POST'])
# def nationalchannels_list(request):
#     if request.method == 'GET':
#         nationalchannel = NationalNewsChannel.objects.all()
#         serializer = NationalNewsChannelSerializer(nationalchannel, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = NationalNewsChannelSerializer(data=request.DATA)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(
#                 serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'POST'])
# def regionalchannels_list(request):
#     if request.method == 'GET':
#         regionalchannel = RegionalNewsChannel.objects.all()
#         serializer = RegionalNewsChannelSerializer(regionalchannel, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = RegionalNewsChannelSerializer(data=request.DATA)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(
#                 serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def ebook_list(request):
    if request.method == 'GET':
        ebook = Ebook.objects.all()
        serializer = EbookSerializer(ebook, many=True)
        resp3 = serializer.data
        ebook_list = {'E-Books':resp3}
        return Response(ebook_list)

    elif request.method == 'POST':
        serializer = EbookSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def Articles(request):
    if request.method == 'GET':
        article = Article.objects.all()
        serializer = ArticleSerializer(article, many=True)
        resp3 = serializer.data
        article_list = {'Articles':resp3}
        return Response(article_list)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.DATA)
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
        resp3 = serializer.data
        magazine_list = {'Magazines':resp3}
        return Response(magazine_list)

    elif request.method == 'POST':
        serializer = MagazineSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'POST'])
# def socialchannels_list(request):
#     if request.method == 'GET':
#         socialchannel = SocialChannel.objects.all()
#         serializer = SocialChannelSerializer(socialchannel, many=True)
#         resp3 = serializer.data
#         socialchannels_list = {'SocialChannels':resp3}
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = SocialChannelSerializer(data=request.DATA)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(
#                 serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def nationalchannels_list(request):
    if request.method == 'GET':

        nationalchannel = NationalNewsChannel.objects.all()
        serializer = NationalNewsChannelSerializer(nationalchannel, many=True)
        resp3 = serializer.data
        national = {'NationalNewsChannels':resp3}

        return Response(national)

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
        resp3 = serializer.data
        regionalchannels_list = {'RegionalNewsChannels':resp3}
        return Response(regionalchannels_list)

    elif request.method == 'POST':
        serializer = RegionalNewsChannelSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def nationalpapers_list(request):
    if request.method == 'GET':

        nationalpaper = NationalNewsPaper.objects.all()
        serializer = NationalNewsPaperSerializer(nationalpaper, many=True)
        resp3 = serializer.data
        national = {'NationalNewsPapers':resp3}

        return Response(national)

    elif request.method == 'POST':
        serializer = NationalNewsPaperSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def regionalpapers_list(request):
    if request.method == 'GET':
        regionalpaper = RegionalNewsPaper.objects.all()
        serializer = RegionalNewsPaperSerializer(regionalpaper, many=True)
        resp3 = serializer.data
        regionalpapers_list = {'RegionalNewsPapers':resp3}
        return Response(regionalpapers_list)

    elif request.method == 'POST':
        serializer = RegionalNewsPaperSerializer(data=request.DATA)
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

class login(APIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data

        username = data.get('username', None)
        password = data.get('password', None)

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                #login(request, user)
                return Response({'detail':" True" },status=status.HTTP_200_OK)
            else:
                return Response({'detail':" False " .format(username) },status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'detail':" False" },status=status.HTTP_404_NOT_FOUND)
        # data = request.data
        # serializer = LoginSerializer(data=data)
        # if serializer.is_valid(raise_exception=True):
        #     new_data = serializer.data
        #     return Response(new_data,status = status.HTTP_200_OK)
        # return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)    

# class UserCreateAPIView(ListCreateAPIView):
#     #serializer_class = UserCreateSerializer

#     @staticmethod
#     def post(self,request, *args, **kwargs):

#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         Application_type = request.POST.get('Application_type')

#         user = User.objects.create_user(username,email,password)
#         user.Application_type = Application_type
#         user.save()

#         token = Token.objects.create(user=user)

#         return Response({'detail':" User has been Created with Token: " + token.key})


def android(request):
    andr_users = Profile.objects.filter(Application_type=1)
    print(andr_users)
    context = {'android':andr_users}
    return render(request,'android_users.html',context)        