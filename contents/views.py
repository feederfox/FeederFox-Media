from django.shortcuts import render,redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.models import Profile
from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView,CreateAPIView
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.http import HttpResponse,Http404
from django.contrib.auth import authenticate,login
from django.contrib import messages
import datetime
from pdf2image import convert_from_path
from django.conf import settings
from pylovepdf.ilovepdf import ILovePdf
import zlib,os,sys,PyPDF2
from rest_framework.authtoken.models import Token
from .forms import PublisherDetailsForm,ArticleForm,UploadContentForm,MainEditionForm,EditionForm,StateForm,PublisherDetailEditForm
from .models import (Ebook,Magazine,SocialChannel,RegionalNewsChannel,NationalNewsChannel,NationalNewsPaper,
                RegionalNewsPaper,Article,NewsPaper,PublisherDetail,Article,Main_Edition,Edition,Sub_Edition,State)
from .serializers import (EbookSerializer,MagazineSerializer,SocialChannelSerializer,NationalNewsChannelSerializer,RegionalNewsChannelSerializer,
    NationalNewsPaperSerializer,RegionalNewsPaperSerializer,ArticleSerializer,SignupSerializer,LoginSerializer,NewsPaperSerializer)




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
        newspaper = NewsPaper.objects.all()
        ebookserializer = EbookSerializer(ebook, many=True,context=context)
        magazineserializer = MagazineSerializer(magazine,many=True,context=context)
        socialserializer = SocialChannelSerializer(socialchannel,many=True,context=context)
        NationalSerializer = NationalNewsChannelSerializer(National,many=True,context=context)
        RegionalSerializer = RegionalNewsChannelSerializer(Regional,many=True,context=context)
        nationalserializer = NationalNewsPaperSerializer(national,many=True,context=context)
        regionalserializer = RegionalNewsPaperSerializer(regional,many=True,context=context)
        articleserializer = ArticleSerializer(article,many=True,context=context)
        newspaperserializer = NewsPaperSerializer(newspaper,many=True,context=context)
        resp = ebookserializer.data
        resp1 = magazineserializer.data
        resp2 = socialserializer.data
        resp3 = NationalSerializer.data
        resp4 = RegionalSerializer.data
        resp5 = nationalserializer.data
        resp6 = regionalserializer.data
        resp7 = articleserializer.data
        resp8 = newspaperserializer.data
        ebk = {'E-Books':resp}
        magaz = {'Magazines':resp1}
        social = {'SocialChannels':resp2}
        national = {'NationalNewsChannels':resp3}
        regional = {'RegionalNewsChannels':resp4}
        nat = {'NationalNewsPapers':resp8}
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
            return Response({"detail": "True"})

        return Response({'detail':'Email already in use'},status=status.HTTP_200_OK)

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

def article(request):
    if request.method=='POST':
        form = ArticleForm(request.POST,request.FILES)
        if form.is_valid():
            article=form.save(commit=False)
            article.save()
    form = ArticleForm()
    context = {'form':form} 
    return render(request,'article_upload.html',context)       


def view_articles(request):
    art = Article.objects.all()
    context = {'articles':art}
    return render(request,'view_articles.html',context)    

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
            # ilovepdf = ILovePdf('project_public_896a1a0eff68b3d3da5e27710febc890_klzpac598631384d2f6025175094ce5ec1f76', verify_ssl=True)
            # task = ilovepdf.new_task('compress')
            # task.add_file('C:\karmashakthi.pdf')
            # task.set_output_folder('C:\FeederFox-Media')
            # task.execute()
            # task.download()
            # task.delete_current_task()
            #pdf = open((os.path.join(settings.BASE_DIR,'media','NewsPapers','Awami_270818.pdf')))
            #pdf = open(pdf1,'rb')
            #print(pdf)
            #compressed_pdf = os.system("ps2pdf -dPDFSETTINGS=/ebook %s reduc/%s" % (pdf1,pdf1))
            # pages = convert_from_path(pdf, 500)
            # for page in pages:
            #     page.save('out.jpg', 'JPEG')
            # writer = PyPDF2.PdfFileWriter()
            # reader = PyPDF2.PdfFileReader(pdf)
            # for i in range(reader.numPages):
            #     page = reader.getPage(i)
            #     page.compressContentStreams()
            #     writer.addPage(page)

            # with open((os.path.join(settings.BASE_DIR,'media','NewsPapers',pdf1_compress)),'wb') as f:
            #     writer.write(f)    
            # compressed_pdf = zlib.compress(pdf1)
            # print(sys.getsizeof(compressed_pdf))
            # compress_ratio = (float(len(pdf)) - float(len(compressed_pdf))) / float(len(pdf))
            b.save()
            name = b.Publishing_Name
            image = b.Add_Logo
            url = b.Add_PDF.url
            mainedition = b.Main_Edition
            subedition = b.Sub_Edition
            user = request.user
            uploaded_at = datetime.datetime.now().strftime("%d-%m-%y %H-%M-%S")
            newspap = NewsPaper.objects.filter(name=name,subedition=subedition)
            newspap.delete()
            newspaper = NewsPaper.objects.create(name=name,image=image,url=url,mainedition=mainedition,
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