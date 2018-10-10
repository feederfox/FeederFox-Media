from django.shortcuts import render,redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.models import Profile,Magazines
from django.contrib.auth.models import User
from rest_framework.generics import (ListCreateAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView,
                RetrieveAPIView,UpdateAPIView)
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.http import HttpResponse,Http404
from django.contrib.auth import authenticate,login
from django.contrib import messages
import datetime
from pdf2image import convert_from_path
from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from rest_framework.renderers import TemplateHTMLRenderer
from pylovepdf.ilovepdf import ILovePdf
from .fusioncharts import FusionCharts
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
import zlib,os,sys,PyPDF2
from rest_framework.authtoken.models import Token
from collections import Counter
from .forms import (PublisherDetailsForm,ArticleForm,UploadContentForm,MainEditionForm,EditionForm,StateForm,
    PublisherDetailEditForm,ArticleUploadForm,PoliticalForumForm,PollingForm,PoliticainArticleForm,UploadMagazineForm,
    NewsChannelForm,EbookUploadForm,PoliticalCommentSystemForm)
from .models import (Ebook,Magazine,SocialChannel,RegionalNewsChannel,NationalNewsChannel,NationalNewsPaper,Dummy,
    Article_upload,ArticleReview,RegionalNewsPaper,Article,NewsPaper,PublisherDetail,Article,Main_Edition,Edition,
    Sub_Edition,State,PoliticalForum,Polling,Vote,PoliticalSurvey,PoliticianArticle,NewsChannel,EbookUpload,
    Article_upload,Vote1,NewsPaperAdmin,PoliticalCommentSystem)
from .serializers import (EbookSerializer,MagazineSerializer,SocialChannelSerializer,NationalNewsChannelSerializer,
    RegionalNewsChannelSerializer,NationalNewsPaperSerializer,RegionalNewsPaperSerializer,ArticleSerializer,
    SignupSerializer,LoginSerializer,NewsPaperSerializer,DummySerializer,PublisherDetailSerializer,
    NewsChannelSerializer,PublisherListSerializer,PoliticalForumSerializer,PoliticalPositionSerializer,
    EbookUpdatedSerializer,ArticleuploadSerializer,NewsPaperEditionSerializer,PollingSerializer,
    PoliticianArticleSerializer,PoliticalSurveySerializer,PoliticalVotingSerializer,PoliticalForumAPISerializer,
    profileUploadSerializer,SignupAPISerializer,PoliticalCommentSerializer)
from .models import Revenue
from django.core.urlresolvers import reverse



@api_view(['GET', 'POST'])
def socialchannels_list(request):
    if request.method == 'GET':
        socialchannel = SocialChannel.objects.all()
        serializer = SocialChannelSerializer(socialchannel, many=True)
        resp3 = serializer.data
        socialchannels_list = {'SocialChannels':resp3}
        return Response(socialchannels_list)

    elif request.method == 'POST':
        serializer = SocialChannelSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def dummy_list(request):
    if request.method == 'GET':
        ebook = Dummy.objects.all()
        print(ebook)
        serializer = DummySerializer(ebook, many=True)
        resp3 = serializer.data
        ebook_list = {'E-Books':resp3}
        return Response(ebook_list)

    elif request.method == 'POST':
        serializer = DummySerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
def ebook_updated(request):
    context = {'request':request}
    if request.method == 'GET':
        ebook = EbookUpload.objects.all()
        serializer = EbookUpdatedSerializer(ebook, many=True,context=context)
        resp3 = serializer.data
        ebook_list = {'E-Books':resp3}
        return Response(ebook_list)

    elif request.method == 'POST':
        serializer = EbookUpdatedSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def politicalforum(request):
    if request.method == 'GET':
        polforum = PoliticalForum.objects.all()
        serializer = PoliticalForumSerializer(polforum, many=True,context={'request':request})
        resp3 = serializer.data
        political = {'PoliticalForum':resp3}
        return Response(political)

    elif request.method == 'POST':
        serializer = PoliticalForumSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# @api_view(['GET', 'POST'])
# def politicalposition(request):
#     if request.method == 'GET':
#         ebook = PoliticalPosition.objects.all()
#         print(ebook)
#         serializer = PoliticalPositionSerializer(ebook, many=True)
#         resp3 = serializer.data
#         ebook_list = {'E-Books':resp3}
#         return Response(ebook_list)

#     elif request.method == 'POST':
#         serializer = PoliticalPositionSerializer(data=request.DATA)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(
#                 serializer.errors, status=status.HTTP_400_BAD_REQUEST)



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


@api_view(['GET', 'POST'])
def newschannels_list(request):
    context = {'request':request}
    if request.method == 'GET':

        newschannel = NewsChannel.objects.all()
        serializer = NewsChannelSerializer(newschannel, many=True,context=context)
        resp3 = serializer.data
        national = {'NationalNewsChannels':resp3}

        return Response(national)

    elif request.method == 'POST':
        serializer = NewsChannelSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'POST'])
def nationalchannels_list(request):
    if request.method == 'GET':

        nationalchannel = NewsChannel.objects.all()
        serializer = NewsChannelSerializer(nationalchannel, many=True)
        resp3 = serializer.data
        national = {'NationalNewsChannels':resp3}

        return Response(national)

    elif request.method == 'POST':
        serializer = NewsChannelSerializer(data=request.DATA)
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


@api_view(['GET'])
def pub(request, pk):
    try:
        product = PublisherDetail.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        context = {
            "request":request
            }
        pub = PublisherDetail.objects.get(pk=pk)
        print(pub)
        pubserializer = PublisherDetailSerializer(pub,context=context)
        name = pub.Name
        news = NewsPaper.objects.filter(name=name)
        print(news)
        newsserializer = NewsPaperSerializer(news,many=True,context=context)
        response = {
            'status': status.HTTP_200_OK,
            'PublisherDetails' : pubserializer.data,
        }
        print(response['PublisherDetails']['Sub_Edition'])
        response['PublisherDetails']['Sub_Edition'] = newsserializer.data
        return Response(response)



@api_view(['GET'])
def publist(request):

    if request.method == 'GET':
        context = {
            "request":request
            }
        pub = PublisherDetail.objects.filter(Type=1)
        print(pub)
        pubserializer = PublisherListSerializer(pub,many=True,context=context)
        response = {
            'status': status.HTTP_200_OK,
            'PublisherDetails' : pubserializer.data,
        }
        a = response['PublisherDetails']
        print(a)
        print(a['url'][0])
        return Response(response)


class pub_list(ListAPIView):

    queryset = PublisherDetail.objects.all()
    serializer_class = PublisherListSerializer

    def get_queryset(self, *args, **kwargs):
        news = NewsPaper.objects.all()
        n = []
        for i in news:
            n.append(i)
        name = n 
        publisherdetails = PublisherDetail.objects.filter(Name__in=name)
        for i in publisherdetails:
            print(i.Name)
        return publisherdetails   




class pub_detail(RetrieveAPIView):
   

    def get_queryset(self, *args, **kwargs):
        context = {
            "request":self.request
            }
        pub_id = self.kwargs.get('pk',None)
        pub = PublisherDetail.objects.get(pk=pub_id)
        print(pub)
        pubserializer = PublisherDetailSerializer(pub,context=context)
        name = pub.Name
        news = NewsPaper.objects.filter(name=name)

        print(news)
        newsserializer = NewsPaperSerializer(news,many=True,context=context)
        response = {
            'status': status.HTTP_200_OK,
            'PublisherDetails' : pubserializer.data,
        }
        print(response['PublisherDetails']['Sub_Edition'])
        response['PublisherDetails']['Sub_Edition'] = newsserializer.data

        return news


@api_view(['GET','POST'])
def pubdetails(request):
    context = {
            "request":request
            }

    news = NewsPaper.objects.all()
    nam = []
    for i in news:
        nam.append(i)
    name = nam 
    pub = PublisherDetail.objects.filter(Type=1)   
    pub_details = PublisherDetail.objects.filter(Name__in=name)
    print(pub_details)
    print(len(pub_details))
    p = []
    for a in pub:
        p.append(a)
    b = p    
    print(b)
    n = NewsPaper.objects.filter(name__in=b)   
    print(n)  
    newsserializer = NewsPaperSerializer(n,many=True,context=context)
    print(newsserializer)
    news = newsserializer.data
    pubserializer = PublisherDetailSerializer(pub,many=True,context=context)
    response = {
            'status': status.HTTP_200_OK,
            'PublisherDetails' : pubserializer.data,
        }

    for c in range( len(pub_details)):
        pass
    response['PublisherDetails'][c]['Sub_Edition'] = newsserializer.data
    a = {'PublisherDetails':response}
    return Response(response)


def edition(request,pk):
    content = PublisherDetail.objects.get(pk=pk)
    name = content.Name
    #url = content.url
    image = content.Add_Logo.url
    mainedition = content.Main_Edition
    sub = content.Sub_Edition.all()
    language = content.Language
    print(language)
    print(sub)
    print(mainedition)
    newspaper = NewsPaper.objects.filter(name=name)
    print(newspaper)
    sub1=[]
    for n in newspaper:
        sub1.append(n.subedition)
    print(sub1)
    context = {'name':name,'image':image,'mainedition':mainedition,'sub':sub,'newspaper':newspaper,'language':language}
    return render(request,'edition.html',context)    


@api_view(['GET', 'POST'])
def publisherdetails(request):
    if request.method == 'GET':
        news = NewsPaper.objects.all()
        print(news)
        nam = []
        for i in news:
            nam.append(i)
        name = nam    
        print(name)
        pub_details = PublisherDetail.objects.get(Name__in=name)
        print(pub_details)
        n = NewsPaper.objects.filter(name=pub_details.Name)
        print(n)
        sub = []
        for a in n:
            sub.append(a.subedition)
        print(sub)
        serializer = PublisherDetailSerializer(pub_details)
        resp3 = serializer.data
        pubdetail = {'PublisherDetails':resp3}
        return Response(pubdetail)

    elif request.method == 'POST':
        serializer = PublisherDetailSerializer(data=request.DATA)
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
def newspapers_list(request):
    if request.method == 'GET':
        newspaper = NewsPaper.objects.all()
        serializer = NewsPaperSerializer(newspaper, many=True)
        resp3 = serializer.data
        print(resp3)
        regionalpapers_list = {'NationalNewsPapers':resp3}
        return Response(regionalpapers_list)

    elif request.method == 'POST':
        serializer = NewsPaperSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
def article_list(request):
    context = {
            "request":request
            }
    article = Article.objects.all()
    articleserializer = ArticleSerializer(article,many=True)
    resp3 = articleserializer.data
    a = {'Articles':resp3}
    return Response(a)

@api_view(['GET', 'POST'])
def contents_list(request):
    if request.method == 'GET':
        context = {
            "request":request
            }
        pub_details = PublisherDetail.objects.filter(Type=1)
        r = {}
        l = []   
        for i in pub_details:
            news = NewsPaper.objects.filter(name=i.Name)
            print(news)
            print(len(news))
            newsserializer = NewsPaperEditionSerializer(news,many=True,context=context)
            if news:
                pub = PublisherDetail.objects.get(Name = i.Name)
                publisherserializer = PublisherDetailSerializer(pub,context=context) 
                resp1 = {}
                resp1 = publisherserializer.data
                resp1['Edition_Count'] = len(news)
                resp1['Sub_Edition'] = newsserializer.data
                l.append(resp1)
        re = {'NationalNewsPapers':l}    
        ebook = Ebook.objects.all()
        National = NewsChannel.objects.all()
        Regional = RegionalNewsChannel.objects.all()
        magazine = Magazine.objects.all()
        socialchannel = SocialChannel.objects.all()
        national = NationalNewsPaper.objects.all()
        regional = RegionalNewsPaper.objects.all()
        article = Article.objects.all()
        newspaper = NewsPaper.objects.all()
        ebook_updated = EbookUpload.objects.all()
        political = PoliticalForum.objects.all()
        ebookserializer = EbookSerializer(ebook, many=True,context=context)
        magazineserializer = MagazineSerializer(magazine,many=True,context=context)
        socialserializer = SocialChannelSerializer(socialchannel,many=True,context=context)
        NationalSerializer = NewsChannelSerializer(National,many=True,context=context)
        RegionalSerializer = RegionalNewsChannelSerializer(Regional,many=True,context=context)
        nationalserializer = NationalNewsPaperSerializer(national,many=True,context=context)
        regionalserializer = RegionalNewsPaperSerializer(regional,many=True,context=context)
        articleserializer = ArticleSerializer(article,many=True,context=context)
        newspaperserializer = NewsPaperSerializer(newspaper,many=True,context=context)
        ebookupdatedserializer = EbookUpdatedSerializer(ebook_updated,many=True,context=context)
        politicalserializer = PoliticalForumSerializer(political,many=True,context=context)
        resp = ebookserializer.data
        resp1 = magazineserializer.data
        resp2 = socialserializer.data
        resp3 = NationalSerializer.data
        resp4 = RegionalSerializer.data
        resp5 = nationalserializer.data
        resp6 = regionalserializer.data
        resp7 = articleserializer.data
        resp8 = newspaperserializer.data
        resp9 = ebookupdatedserializer.data
        resp10 = politicalserializer.data
        #ebk = {'E-Books':resp}
        magaz = {'Magazines':resp1}
        social = {'SocialChannels':resp2}
        national = {'NationalNewsChannels':resp3}
        regional = {'RegionalNewsChannels':resp4}
        nat = {'NationalNewsPapers':resp8}
        reg = {'RegionalNewsPapers':resp6}
        art = {'Articles':resp7}
        pol = {'PoliticalForum':resp10}
        ebook = {'E-Books':resp9}
        b = regional.copy()
        b.update(national)
        news = {'NewsChannels':b}
        c = reg.copy()
        c.update(re)
        paper = {'NewsPapers':c}
        a = ebook.copy()
        a.update(magaz)
        a.update(social)
        a.update(news)
        a.update(paper)
        a.update(art)
        a.update(pol)
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


class articleuploadapi(APIView):
    serializer_class = ArticleuploadSerializer

    def post(self,request,*args,**kwargs):
        data = request.data
        title = data['title']
        image = data['image']
        description = data['description']
        Author = data['Author']
        url = data['url']
        serializer = ArticleuploadSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail':serializer.data})

        return Response({'detail':"Error"})    

class signup(APIView):
    serializer_class = SignupSerializer
    def post(self,request, *args, **kwargs):
        data = request.data
        email = data['email']
        print(email)
        username = data['username']
        print(username)
        serializer = SignupSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print(serializer)
            return Response({"detail": "True" })

        return Response({'detail':'Email already in use'},status=status.HTTP_200_OK)


class signupapi(APIView):
    serializer_class = SignupAPISerializer
    def post(self,request, *args, **kwargs):
        data = request.data
        email = data['email']
        print(email)
        serializer = SignupAPISerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            try:
                a = Profile.objects.get(email=email)
            except Exception as e:
                return Response({'status_code':0,'detail':"User not found" },status=status.HTTP_200_OK)
            username = a.username
            Mobile = a.Mobile
            Profile_Picture = a.Profile_Picture
            Social_login = 0
            d = {'email':email,'username':username,'Mobile':Mobile,'Profile_Picture':Profile_Picture.url,
            'Social_login':Social_login}
            print(d)
            s = SignupAPISerializer(data=d)
            if s.is_valid():
                s.save()
            response = {
                'status_code':1,
                'detail':s.data,
            }
            response['detail']['Social_login'] = 0
            return Response(response)
        response = {
            'status_code' : 0,
            'detail':'Email already in use',
        }
        return Response(response,status=status.HTTP_200_OK)


class newspaperedition(APIView):
    serializer_class = NewsPaperEditionSerializer

    def post(self,request, *args, **kwargs):
        data = request.data
        name = data.get('name',None)
        subedition = data.get('subedition')
        print(name)
        print(subedition)
        try:
            newspaper = NewsPaper.objects.get(name=name,subedition=subedition)
            print(newspaper)
        except Exception as e:
            return Response({'detail':"NewsPaper not found" },status=status.HTTP_200_OK)

        if newspaper:
            newsserializer = NewsPaperEditionSerializer(newspaper,context={'request':request})
            response = {
                'status': status.HTTP_200_OK,
                'PublisherDetails' : newsserializer.data,
            }
            return Response(response)
                
class login(APIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data

        email = data.get('email', None)
        password = data.get('password', None)
        print(email)
        try:
            username = User.objects.get(email=email).username
            print(username)
        except Exception as e:
            return Response({'detail':"User not found" },status=status.HTTP_200_OK)
        print(username)
        if username:
            user = authenticate(username=username, password=password)
            print(user)

            if user is not None:
                if user.is_active:
                    #login(request, user)
                    return Response({'detail':"True" },status=status.HTTP_200_OK)
                else:
                    return Response({'detail':"False "},status=status.HTTP_200_OK)
            else:
                return Response({'detail':"False" },status=status.HTTP_200_OK)
        return Response({'detail':" False" },status=status.HTTP_200_OK)



class loginapi(APIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        email = data.get('email', None)
        password = data.get('password', None)
        email = data['email']
        try:
            a = Profile.objects.get(email=email)
        except Exception as e:
            return Response({'status_code':0,'detail':"User not found" },status=status.HTTP_200_OK)
        username = a.username
        Mobile = a.Mobile
        Social_login = 0
        print(Mobile)
        d = {'email':email,'username':username,'Mobile':"",'Profile_Picture':"",'Social_login':Social_login}       
        if a.Mobile:
            d = {'email':email,'username':username,'Mobile':str(Mobile),'Profile_Picture':"",'Social_login':Social_login} 
            if a.Profile_Picture:
                Profile_Picture = a.Profile_Picture
                d = {'email':email,'username':username,'Mobile':str(Mobile),'Profile_Picture':Profile_Picture.url,
                'Social_login':Social_login}


        serializer = SignupAPISerializer(data=d)
        if serializer.is_valid():
            serializer.save()
            resp = serializer.data
        try:
            username = User.objects.get(email=email).username
            print(username)
        except Exception as e:
            return Response({'status_code':0,'detail':{"message":"User Not Found"} },status=status.HTTP_200_OK)
        print(username)
        if username:
            user = authenticate(username=username, password=password)
            print(user)

            if user is not None:
                if user.is_active:
                    response = {'status_code':1,'detail': serializer.data}
                    response['detail']['Social_login'] = 0
                    response['detail']['user_id'] = user.id
                    return Response(response,status=status.HTTP_200_OK)
                else:
                    return Response({'status_code':0,'detail':{"message":"False"}},status=status.HTTP_200_OK)
            else:
                return Response({'status_code':0,'detail':{"message":"False"} },status=status.HTTP_200_OK)
        return Response({'status_code':0,'detail':{"message":"False"} },status=status.HTTP_200_OK)


def android(request):
    andr_users = Profile.objects.filter(Application_type=1)
    print(andr_users)
    context = {'android':andr_users}
    return render(request,'android_users.html',context)

def pub_details(request):    
    if request.method == 'POST':
        form = PublisherDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            a = form.save(commit=False)
            a.user=request.user
            print(a.user)
            a.save()
            form.save_m2m()
            messages.success(request,'Successfully Added')      
    form = PublisherDetailsForm()
    mainedition = Main_Edition.objects.all()
    subedition = Edition.objects.all()
    state = State.objects.all()
    context = {'form':form,'mainedition':mainedition,'subedition':subedition,'state':state}  
    return render(request,'publisher_details.html',context)        

@login_required(login_url='/accounts/login/')
def article(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form = ArticleUploadForm(request.POST,request.FILES)
            if form.is_valid():
                article=form.save(commit=False)
                article.save()
                messages.success(request,'Article has been Uploaded Successfully')
        form = ArticleUploadForm()
        context = {'form':form} 
        return render(request,'article_upload.html',context)  
    return redirect('accounts:login')         


def view_articles(request,pk):
    art = Article.objects.get(pk=pk)
    title = art.title
    description = art.description
    image = art.image
    url = art.url
    author = art.author
    context = {'articles':art}
    return render(request,'article1.html',locals())    


def view_pub_details(request):
    pub_details = PublisherDetail.objects.all() 
    context = {'details':pub_details}
    return render(request,'publisher_details_list.html',context)   

def my_papers(request):
    papers = PublisherDetail.objects.filter(Type=1,user=request.user)
    print(request.user)
    context = {'papers':papers}
    return render(request,'mypapers.html',context)

def my_magazines(request):
    magazine = PublisherDetail.objects.filter(Type=2,user=request.user)
    print(request.user)
    context = {'magazines':magazine}
    return render(request,'mymagazines.html',context)    

def load_mainedition(request):
    State_id = request.GET.get('State')
    mainedition = Main_Edition.objects.filter(State_id=State_id)
    return render(request, 'main_edition_dropdownlist.html', {'maineditions': mainedition})   

def load_subedition(request):
    State_id = request.GET.get('State')
    subedition = Edition.objects.filter(State_id=State_id)
    return render(request, 'subedition_dropdownlist.html', {'subeditions': subedition})         


def upload(request,pk):
    a = PublisherDetail.objects.get(pk=pk)
    d = [i for i in a.Sub_Edition.all() ]
    length = len(a.Sub_Edition.all())
    n = a.Name
    # s = Sub_Edition.objects.all()
    # print(s)
    # s.delete()
    # print(s)
    for x in range(0,length):
        #e.delete()
        e = Sub_Edition.objects.create(Edition=d[x],Name=n)
        t = Sub_Edition.objects.filter(Name=n,Edition=d[x])
        print(t)
        for u in Sub_Edition.objects.filter(Name=n,Edition=d[x]).values_list("id", flat=True).distinct():
            pass
        Sub_Edition.objects.filter(pk__in=Sub_Edition.objects.filter(Name=n,Edition=d[x]).values_list('id',flat=True)[1:]).delete()
        print(n)
    print(n)
    y = Sub_Edition.objects.filter(Name=n).distinct()
    print(y)

    if request.method=='POST':
        form = UploadContentForm(request.POST,request.FILES)
        print('HI')
        if form.is_valid():
            print('IS')
            b=form.save(commit=False)
            b.Publishing_House = a.Name
            b.Publishing_Name = a.Name
            b.Add_Logo = a.Add_Logo
            b.State = a.State
            b.Languages = a.Language
            b.user = request.user
            b.Main_Edition = a.Main_Edition
            b.Sub_Edition = form.cleaned_data.get('Sub_Editions')
            print(form.cleaned_data.get('Sub_Editions'))
            print(b.Add_PDF)
            pdf1 = b.Add_PDF
            print(pdf1)
            b.save()
            name = b.Publishing_Name
            image = b.Add_Logo
            url = b.Add_PDF.url
            mainedition = b.Main_Edition
            subedition = b.Sub_Edition
            user = request.user
            uploaded_at = datetime.datetime.now().strftime("%d-%m-%y %H-%M-%S")
            newspap = NewsPaperAdmin.objects.filter(name=name,subedition=subedition)
            newspap.delete()
            newspaper = NewsPaperAdmin.objects.create(name=name,image=image,url=url,mainedition=mainedition,
                                    subedition=subedition,user=user,Uploaded_at=uploaded_at)
            print(newspaper)

            messages.success(request,'Successfully Uploaded')
            form = UploadContentForm()
            c = Sub_Edition.objects.all()
            c.delete()


    form = UploadContentForm()
    return render(request,'upload_content.html',{'form':form})

def edition(request,pk):
    content = PublisherDetail.objects.get(pk=pk)
    name = content.Name
    #url = content.url
    image = content.Add_Logo.url
    mainedition = content.Main_Edition
    sub = content.Sub_Edition.all()
    language = content.Language
    print(language)
    print(sub)
    print(mainedition)
    newspaper = NewsPaper.objects.filter(name=name)
    print(newspaper)
    sub1=[]
    for n in newspaper:
        sub1.append(n.subedition)
    print(sub1)
    context = {'name':name,'image':image,'mainedition':mainedition,'sub':sub,'newspaper':newspaper,'language':language}
    return render(request,'edition.html',context)    


def addmainedition(request):
    if request.method=='POST':
        form = MainEditionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('content:add')

    form = MainEditionForm()
    return render(request,'addmainedition.html',{'form':form})

def addsubedition(request):
    if request.method=='POST':
        form = EditionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('content:add')

    form = EditionForm()
    return render(request,'addsubedition.html',{'form':form})                        


def addstate(request):
    if request.method=='POST':
        form = StateForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('content:add')

    form = StateForm()
    return render(request,'addstate.html',{'form':form})            

def publisherdetailedit(request,pk):
    pub = PublisherDetail.objects.get(pk=pk)  
    print(pub)
    print(pub.Type)
    pub_form = PublisherDetailEditForm(instance=pub)
    if request.method=='POST':
        form = PublisherDetailEditForm(request.POST,request.FILES, instance=pub)
        if form.is_valid():
            pub = form.save()
            pub.save()
            print(pub.Type)
            if pub.Type=='1':
                return redirect('content:my_papers')
            else:
                return redirect('content:my_magazines')    

    form = PublisherDetailEditForm()
    return render(request,'publisherdetail_editform.html',{'form':pub_form})

def deletepapers(request,pk):
    paper = PublisherDetail.objects.filter(Type=1,user=request.user).get(pk=pk)
    print(paper)
    paper.delete()
    return redirect('content:my_papers')

def deletemagazines(request,pk):
    magazine = PublisherDetail.objects.filter(Type=2,user=request.user).get(pk=pk)
    print(magazine)
    magazine.delete()
    return redirect('content:my_magazines')    

def political(request):
    if request.method=='POST':
        form = PoliticalForumForm(request.POST,request.FILES)
        if form.is_valid:
            form.save()
            messages.success(request,'Successfully Updated')

    form = PoliticalForumForm()
    return render(request,'political.html',{'form':form})

def politicalmodal(request,pk):
    political = PoliticalForum.objects.get(pk=pk)
    name = political.Name
    synopsis = political.Synopsis
    image = political.Image
    Educational_Qualification = political.Educational_Qualification
    Family_History = political.Family_History
    projects_taken = political.Projects_Taken
    video_link = political.video_link
    poll = Polling.objects.get(Name=name)
    polart = PoliticianArticle.objects.filter(Name=name)
    polcomment = PoliticalCommentSystem.objects.filter(name=name)
    rating = []
    for p in polcomment:
        r = int(p.ratings)
        rating.append(r)
    if rating:    
        avg_rating = (sum(rating)/len(rating))
    else:
        avg_rating = 0    
    rating_count = Counter(rating)
    rc_5 = rating_count[5]
    rc_4 = rating_count[4]
    rc_3 = rating_count[3]
    rc_2 = rating_count[2]
    rc_1 = rating_count[1]
    dataSource = {}
    dataSource = {  
        "chart": {
        "caption": "FeederFox-Media",
        "xAxisName": "Month",
        "yAxisName": "Percentage in (%)",
        "numberSuffix": "%",
        "showalternatehgridcolor": "0",
        "plotgradientcolor": "",
        "showplotborder": "0",
        "showBorder": "0",
        "borderColor": "#666666",
        "borderThickness": "4",
        "borderAlpha": "80",
        "bgColor": "#DDDDDD",
        "bgAlpha": "50",
        "plotHoverEffect":"1",
        "valuePadding": "5",
        "theme": "fusion",
      },
      "data": [{
        "label": "Yes",
        "value": ((poll.Upvote/(poll.Upvote+poll.DownVote))*100),
        "color": "#9D2125",
      }, {
        "label": "No",
        "value": (poll.DownVote/(poll.Upvote+poll.DownVote))*100,
        "color": "#000",
      }]
      }



    column2D = FusionCharts("column2D", "ex1" , "550", "350", "chart-1", "json", dataSource)

    dataSourc = {}
    dataSourc = {
    "chart": {
    "caption": "FeederFox-Media",
    "yaxisname": "Percentage (in %)",
    "numbersuffix": " %",
    "rotatelabels": "1",
    "setadaptiveymin": "1",
    "showalternatehgridcolor": "0",
    "plotgradientcolor": "",
    "showplotborder": "0",
    "showBorder": "0",
    "borderColor": "#666666",
    "borderThickness": "4",
    "borderAlpha": "80",
    "bgColor": "#DDDDDD",
    "bgAlpha": "50",
    "plotHoverEffect":"1",
    "valuePadding": "5",
    "theme": "fusion",
    },
    "data": [
    {
      "label": 'April',
      "value": ((poll.Upvote/(poll.Upvote+poll.DownVote))*100)
    },
    {
      "label": "May",
      "value": "80.0",
    },
    {
      "label": "June",
      "value": "86.5",
    },
    {
      "label": "July",
      "value": "81.5",
    },
    {
      "label": "August",
      "value": "76.5",
    },
    {
      "label": "Sept",
      "value": "89.5",
    }

    ]
    }

    chartObj = FusionCharts('line','ex2','600','350','chart-2','json',dataSourc)


    
    context = {'name':name,'synopsis':synopsis,'image':image,'Educational_Qualification':Educational_Qualification,
    'video_link':video_link,'Family_History':Family_History,'projects_taken':projects_taken,'poll':poll,
    'output':column2D.render(),'polart':polart,'out':chartObj.render(),'polcomment':polcomment,'avg_rating':avg_rating,
    'rating_count':rating_count,'rc_5':rc_5,'rc_4':rc_4,'rc_3':rc_3,'rc_2':rc_2,'rc_1':rc_1,'political':political}
    return render (request,'political_forum.html',context)


@login_required(login_url='/accounts/login/')
def upvote(request,pk):
    poll = PoliticalSurvey.objects.get(pk=pk)
    name = poll.Name
    print(name)
    p = PoliticalSurvey.objects.filter(Name=poll.Name)
    print(p)
    a = Polling.objects.get(Name=name)
    print(a)
    vote = Vote.objects.all()
    vo = Vote.objects.filter(user=request.user,Poll_Question=poll.Poll_Question)
    print(vo)
    if not vo:
        user = request.user
        v = Vote.objects.create(user=user,Poll_Question=poll.Poll_Question)
        v.save()
        a.Upvote += 1
        a.save()
        messages.success(request,'Your Response has been Saved')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    messages.error(request,'We have already received your response for this Question')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='/accounts/login/')
def downvote(request,pk):
    poll = PoliticalSurvey.objects.get(pk=pk)
    name = poll.Name
    print(name)
    p = PoliticalSurvey.objects.filter(Name=poll.Name)
    print(p)
    a = Polling.objects.get(Name=name)
    print(a)
    vote = Vote.objects.all()
    vo = Vote.objects.filter(user=request.user,Poll_Question=poll.Poll_Question)
    print(vo)
    if not vo:
        user = request.user
        v = Vote.objects.create(user=user,Poll_Question=poll.Poll_Question)
        v.save()
        a.DownVote += 1
        a.save()
        messages.success(request,'Your Response has been Saved')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    messages.error(request,'We have already received your response for this Question')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='/accounts/login/')
def politicalsurvey(request,pk):
    pol_name = PoliticalForum.objects.get(pk=pk)
    name = pol_name.Name
    print(name)
    polsurvey = PoliticalSurvey.objects.filter(Name=name)
    return render(request,'politicalsurvey.html',{'polsurvey':polsurvey,'name':name})      

def chart(request):
    # Chart data is passed to the `dataSource` parameter, as dict, in the form of key-value pairs.
    dataSource = {}
    # dataSource['chart'] = { 
    #     "caption": "FeederFox-Media",
    #         "xAxisName": "Month",
    #         "yAxisName": "Percentage in (%)",
    #         "numberPrefix": "%",
    #         "theme": "zune"
    #     }

    # The data for the chart should be in an array where each element of the array is a JSON object
    # having the `label` and `value` as key value pair.

    dataSource['data'] = []
    
    # Iterate through the data in `Revenue` model and insert in to the `dataSource['data']` list.
    for poll in Polling.objects.filter(Name='Rahul Gandhi'):
        data = {}
        val = {}
      #   "data": [{
      #   "label": "Batman",
      #   "value": "85000"
      # }, {
      #   "label": "Wolverine",
      #   "value": "82000"
      # }]

    dataSource = {  
        "chart": {
        "caption": "FeederFox-Media",
        "xAxisName": "Month",
        "yAxisName": "Percentage in (%)",
        "numberSuffix": "%",
        "showalternatehgridcolor": "0",
        "plotgradientcolor": "",
        "showplotborder": "0",
        "showBorder": "0",
        "borderColor": "#666666",
        "borderThickness": "4",
        "borderAlpha": "80",
        "bgColor": "#DDDDDD",
        "bgAlpha": "50",
        "plotHoverEffect":"1",
        "valuePadding": "5",
        "theme": "fusion",
      },
      "data": [{
        "label": "Yes",
        "value": ((poll.Upvote/(poll.Upvote+poll.DownVote))*100),
        "color": "#9D2125",
      }, {
        "label": "No",
        "value": (poll.DownVote/(poll.Upvote+poll.DownVote))*100,
        "color": "#000",
      }]
      }
                             
    column2D = FusionCharts("column2D", "ex1" , "700", "450", "chart-1", "json", dataSource)
    return render(request, 'modal.html', {'output': column2D.render(),'out':chartObj.render(),}) 


def linechart(request):

    for poll in Polling.objects.filter(Name='Rahul Gandhi'):
        pass
    dataSourc = {}
    dataSourc = {
    "chart": {
    "caption": "FeederFox-Media",
    "yaxisname": "Percentage (in %)",
    "numbersuffix": " %",
    "rotatelabels": "1",
    "setadaptiveymin": "1",
    "showalternatehgridcolor": "0",
    "plotgradientcolor": "",
    "showplotborder": "0",
    "showBorder": "0",
    "borderColor": "#666666",
    "borderThickness": "4",
    "borderAlpha": "80",
    "bgColor": "#DDDDDD",
    "bgAlpha": "50",
    "plotHoverEffect":"1",
    "valuePadding": "5",
    "theme": "fusion",
    },
    "data": [
    {
      "label": 'Yes',
      "value": ((poll.Upvote/(poll.Upvote+poll.DownVote))*100)
    },
    {
      "label": "No",
      "value": ((poll.DownVote/(poll.Upvote+poll.DownVote))*100),
    },
    {
      "label": "Cantsay",
      "value": "86.5",
    }
    ,
    {
      "label": "Cantsay",
      "value": "82.5",
    }
    ,
    {
      "label": "Cantsay",
      "value": "76.5",
    }
    ,
    {
      "label": "Cantsay",
      "value": "96.5",
    }
    ]
    }

    chartObj = FusionCharts('line','ex1','600','400','chart-1','json',dataSourc)
    return render(request, 'modal.html', {'output': chartObj.render()})

def review(request):
    review = ArticleReview.objects.all()
    print(review)
    return render(request,'review_view.html',{'review':review})


def politicianarticle(request):
    if request.method=='POST':
        form = PoliticainArticleForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Successfully Uploaded')
            form = PoliticainArticleForm()    

    form = PoliticainArticleForm()
    return render(request,'politicianarticleupload.html',{'form':form})        

def polling(request):
    if request.method=='POST':
        form = PollingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Successfully Uploaded')

    form = PollingForm()
    return render(request,'polling.html',{'form':form})        


def newschannelsupload(request):
    if request.method=='POST':
        form = NewsChannelForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Successfully Added')

    form = NewsChannelForm()
    return render(request,'uploadnewschannels.html',{'form':form})        

def ebookupload(request):
    if request.method=='POST':
        form = EbookUploadForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Successfully Uploaded')

    form = EbookUploadForm()
    return render(request,'uploadebooks.html',{'form':form})            


def viewebook(request,pk):
    ebook = EbookUpload.objects.get(pk=pk)
    pdf = ebook.pdf
    name = ebook.name
    author = ebook.author
    request.session['ebook_id'] = ebook.id
    context = {'pdf':pdf,'name':name}
    return redirect(reverse('payment:process'))
    #return render(request,'viewebooks.html',context)

class politicalforumdetails(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'political_forum_api.html'

    def get(self, request,pk):
        political = PoliticalForum.objects.get(pk=pk)
        name = political.Name
        synopsis = political.Synopsis
        image = political.Image
        Educational_Qualification = political.Educational_Qualification
        Family_History = political.Family_History
        projects_taken = political.Projects_Taken
        video_link = political.video_link
        poll = Polling.objects.get(Name=name)
        polart = PoliticianArticle.objects.filter(Name=name)
        print(polart)
        dataSource = {}
        dataSource = {  
            "chart": {
            "caption": "FeederFox-Media",
            "xAxisName": "Month",
            "yAxisName": "Percentage in (%)",
            "numberSuffix": "%",
            "showalternatehgridcolor": "0",
            "plotgradientcolor": "",
            "showplotborder": "0",
            "showBorder": "0",
            "borderColor": "#666666",
            "borderThickness": "4",
            "borderAlpha": "80",
            "bgColor": "#DDDDDD",
            "bgAlpha": "50",
            "plotHoverEffect":"1",
            "valuePadding": "5",
            "theme": "fusion",
          },
          "data": [{
            "label": "Yes",
            "value": ((poll.Upvote/(poll.Upvote+poll.DownVote))*100),
            "color": "#9D2125",
          }, {
            "label": "No",
            "value": (poll.DownVote/(poll.Upvote+poll.DownVote))*100,
            "color": "#000",
          }]
          }



        column2D = FusionCharts("column2D", "ex1" , "550", "350", "chart-1", "json", dataSource)

        dataSourc = {}
        dataSourc = {
        "chart": {
        "caption": "FeederFox-Media",
        "yaxisname": "Percentage (in %)",
        "numbersuffix": " %",
        "rotatelabels": "1",
        "setadaptiveymin": "1",
        "showalternatehgridcolor": "0",
        "plotgradientcolor": "",
        "showplotborder": "0",
        "showBorder": "0",
        "borderColor": "#666666",
        "borderThickness": "4",
        "borderAlpha": "80",
        "bgColor": "#DDDDDD",
        "bgAlpha": "50",
        "plotHoverEffect":"1",
        "valuePadding": "5",
        "theme": "fusion",
        },
        "data": [
        {
          "label": 'April',
          "value": ((poll.Upvote/(poll.Upvote+poll.DownVote))*100)
        },
        {
          "label": "May",
          "value": "80.0",
        },
        {
          "label": "June",
          "value": "86.5",
        },
        {
          "label": "July",
          "value": "81.5",
        },
        {
          "label": "August",
          "value": "76.5",
        },
        {
          "label": "Sept",
          "value": "89.5",
        }

        ]
        }

        chartObj = FusionCharts('line','ex2','600','350','chart-2','json',dataSourc)


        
        context = {'name':name,'synopsis':synopsis,'image':image,'Educational_Qualification':Educational_Qualification,'video_link':video_link,
            'Family_History':Family_History,'projects_taken':projects_taken,'poll':poll,'output':column2D.render(),'polart':polart,
                    'out':chartObj.render()}
        #queryset = Profile.objects.all()
        return Response(context)



@api_view(['GET'])
def politicalforumapi(request, pk):
    try:
        pol = PoliticalForum.objects.get(pk=pk)
        print(pol)
    except pol.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        context = {
            "request":request
        }
        politicianserializer = PoliticalForumSerializer(pol,context=context)    
        poll = Polling.objects.get(Name=pol.Name)
        pollserializer = PollingSerializer(poll,context=context)
        polart = PoliticianArticle.objects.filter(Name=pol.Name)   
        polartserializer = PoliticianArticleSerializer(polart,many=True,context=context) 
        polsurvey = PoliticalSurvey.objects.filter(Name=pol.Name)
        polsurveyserializer = PoliticalSurveySerializer(polsurvey,many=True,context=context)
        response = {
            'status':status.HTTP_200_OK,
            'Polling':pollserializer.data,
            'Politician_data':politicianserializer.data,
            'Politician_Articles':polartserializer.data,
            'Politician_Survey':polsurveyserializer.data,
        }

    return Response(response)    



@api_view(['GET'])
def politicalapi(request):
    if request.method == 'GET':
        context = {'request':request}
        polforum = PoliticalForum.objects.all()
        resp = {}
        r = {}
        l = []   
        for i in polforum:
            resp[i] = i
            political = PoliticalForum.objects.get(Name = resp[i].Name)
            politicalserializer = PoliticalForumAPISerializer(political,context=context)
            poll = Polling.objects.get(Name=resp[i].Name)
            pollserializer = PollingSerializer(poll,context=context)
            polart = PoliticianArticle.objects.filter(Name=resp[i].Name)   
            polartserializer = PoliticianArticleSerializer(polart,many=True,context=context) 
            polsurvey = PoliticalSurvey.objects.filter(Name=resp[i].Name)
            polsurveyserializer = PoliticalSurveySerializer(polsurvey,many=True,context=context)
            polcomment = PoliticalCommentSystem.objects.filter(name = i.Name)
            polcommentserializer = PoliticalCommentSerializer(polcomment,many=True,context=context)
            rating = []
            for p in polcomment:
                r = int(p.ratings)
                rating.append(r)
            if rating:    
                avg_rating = (sum(rating)/len(rating))
            else:
                avg_rating = 0
            resp1 = {}
            resp1 = politicalserializer.data
            resp1['Polling'] = pollserializer.data
            resp1['Polling']['Like'] = (poll.Upvote/(poll.Upvote+poll.DownVote))*100
            resp1['Polling']['Dislike'] = (poll.DownVote/(poll.Upvote+poll.DownVote))*100
            resp1['Politician_Articles'] = polartserializer.data
            resp1['Politician_Survey'] = polsurveyserializer.data
            resp1['Politician_Comments'] = polcommentserializer.data
            resp1['Politician_Rating'] = avg_rating
            #if resp1['Politician_Comments']['image'] == null:
            #resp1['Politician_Comments']['Dislike'] = ""
            l1 = resp1
            l.append(resp1)
        re = {'Politician_data':l}    
        return Response(re)



class politicalvotingapi(APIView):
    serializer_class = PoliticalVotingSerializer

    def post(self,request,*args,**kwargs):
        data = request.data
        question_id = data['question_id']
        opinion = data['opinion']
        email = data['email']
        print(question_id)
        print(opinion)
        print(email)
        try:
            poll = PoliticalSurvey.objects.get(pk=question_id)
            print(poll)
        except poll.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        name = poll.Name
        print(name)
        a = Polling.objects.get(Name=name)
        print(a)
        vote = Vote1.objects.all()
        username = User.objects.get(email=email).username
        print(username)
        user = username
        vo = Vote1.objects.filter(user = user,Poll_Question=poll.Poll_Question)
        print(vo)
        if not vo:
            user = username
            print(user)
            v = Vote1.objects.create(user=user,Poll_Question=poll.Poll_Question)
            v.save()
            if opinion == '0':
                a.DownVote += 1
            elif opinion == '1':
                a.Upvote += 1
            a.save()
            response = {
                'status':1,
                'detail':'Your Response has been Saved !!!',
            }
            return Response(response)        

        resp = {
            'status':0,
            'detail':'We have already received your Response',
        }
        return Response(resp)

# news = NewsPaper.objects.filter(name=name)
#         print(news)
#         newsserializer = NewsPaperSerializer(news,many=True,context=context)
#         response = {
#             'status': status.HTTP_200_OK,
#             'PublisherDetails' : pubserializer.data,
#         }
#         print(response['PublisherDetails']['Sub_Edition'])
#         response['PublisherDetails']['Sub_Edition'] = newsserializer.data
#         return Response(response)


@api_view(['GET'])
def publishersapi(request):
    if request.method == 'GET':
        context = {'request':request}
        pub_details = PublisherDetail.objects.filter(Type=1)
        r = {}
        l = []   
        for i in pub_details:
            news = NewsPaper.objects.filter(name=i.Name)
            print(news)
            print(len(news))
            newsserializer = NewsPaperEditionSerializer(news,many=True,context=context)
            if news:
                pub = PublisherDetail.objects.get(Name = i.Name)
                publisherserializer = PublisherDetailSerializer(pub,context=context) 
                resp1 = {}
                resp1 = publisherserializer.data
                resp1['Edition_Count'] = len(news)
                resp1['Sub_Edition'] = newsserializer.data
                l.append(resp1)
        re = {'Publisher_details':l}    
        return Response(re)

@login_required(login_url='/accounts/login/')
def politicalcomment(request,pk):
    political = PoliticalForum.objects.get(pk=pk)
    print(political)
    name = political.Name
    print(political.id)
    id = political.id
    print(id)
    if request.method=='POST':
        form = PoliticalCommentSystemForm(request.POST,request.FILES)
        if form.is_valid():
            a = form.save(commit=False)
            a.user = request.user
            print(request.user.email)
            p = Profile.objects.get(email=request.user.email)
            if p.Profile_Picture is 'null':
                a.image = ""
            else:
                a.image = p.Profile_Picture
            print(p.Profile_Picture)
            print('HI')    
            print(a.image)       
            a.name = name
            a.save()
            messages.success(request,'Comment has been Uploaded')
            #return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            
    form = PoliticalCommentSystemForm()
    return render(request,'politicalcomment.html',{'form':form,'id':str(id)})        



class profileuploadapi(UpdateAPIView):
    queryset = Profile.objects.filter(Account_type='2')
    serializer_class = profileUploadSerializer

    def post(self,request,*args,**kwargs):
            data = request.data
            user = data['user']
            username = data['username']
            email = data['email']
            Company_Name = data['Company_Name']
            Firstname = data['Firstname']
            Lastname = data['Lastname']
            Address = data['Address']
            Mobile = data['Mobile']
            password1 = data['password1']
            password2 = data['password2']
            Application_type = data['Application_type']
            instance = self.get_object()
            instance.username = request.data.get("username")
            instance.save()
            serializer = self.get_serializer(instance=instance,data=data)
            if serializer.is_valid():
                self.perform_update(serializer)
                return Response({'detail':serializer.data})

            return Response({'detail':"Error"})



@api_view(['GET', 'POST'])
def profile_updated(request):
    context = {'request':request}
    if request.method == 'GET':
        profile = Profile.objects.filter(Account_type='2')
        serializer = profileUploadSerializer(profile, many=True,context=context)
        resp3 = serializer.data
        profile_list = {'profile':resp3}
        return Response(profile_list)

    elif request.method == 'POST':
        serializer = profileUploadSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def newspapers_admin(request):
    news = NewsPaperAdmin.objects.all()
    return render(request,'view_newspapers_admin.html',{'news':news})

def newspapers_uploadto_web(request,pk):
    b = NewsPaperAdmin.objects.get(pk=pk)
    newspap = NewsPaper.objects.filter(name=b.name,subedition=b.subedition)
    newspap.delete()
    newspaper = NewsPaper.objects.create(name=b.name,image=b.image,url=b.url,mainedition=b.mainedition,
        subedition=b.subedition,user=b.user,Uploaded_at=b.Uploaded_at)    
    messages.success(request,'NewsPaper has Successfully Uploaded to Website')
    return redirect('content:newspapers_admin')  