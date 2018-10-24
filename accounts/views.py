import os,zlib,sys
import PyPDF2
from django.conf import settings
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect,HttpResponse
from .forms import ( SignUpForm,PostForm,PublisherForm,PublisherEditForm,CustomerEditForm,CustomerForm,MagazineForm,
    PoliticianSignUpForm,AdvertiserForm,AdvertiserEditForm,PublisherSignUpForm,AdvertiserSignUpForm,CustomerSignUpForm,
    ProfileEditForm)
from .models import Profile,Post,NewsPap
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from contents.models import NewsPaper,Magazine,Article_upload,Article
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from django.views.generic.base import TemplateView


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.Account_type = form.cleaned_data.get('Account_type')
            user.profile.username = form.cleaned_data.get('username')
            user.profile.email = form.cleaned_data.get('email')
            print(user.profile.Account_type)
            u = User.objects.filter(email=user.profile.email)
            if u:
                messages(request,'This Email is Already Registered')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('accounts:login')
    else:
        form = SignUpForm()
    return render(request, 'account/signup.html', {'form': form})

def publisher_signup(request):
    if request.method=='POST':
        form = PublisherSignUpForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.Account_type = 1
            user.profile.username = form.cleaned_data.get('username')
            user.profile.email = form.cleaned_data.get('email')
            user.profile.Profile_Picture = form.cleaned_data.get('Profile_Picture')
            user.profile.Mobile = form.cleaned_data.get('Mobile')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            messages.success(request,'Successfully Registered')
            return redirect('accounts:login')
    else:
        form = PublisherSignUpForm()
    return render (request, 'account/publishersignup.html', {'form':form})


def customer_signup(request):
    if request.method=='POST':
        form = CustomerSignUpForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.Account_type = 2
            user.profile.username = form.cleaned_data.get('username')
            user.profile.email = form.cleaned_data.get('email')
            user.profile.Profile_Picture = form.cleaned_data.get('Profile_Picture')
            user.profile.Mobile = form.cleaned_data.get('Mobile')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            messages.success(request,'Successfully Registered')
            return redirect('accounts:login')
    else:
        form = CustomerSignUpForm()
    return render (request, 'account/signup.html', {'form':form})



def advertiser_signup(request):
    if request.method=='POST':
        form = AdvertiserSignUpForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.Account_type = 3
            user.profile.username = form.cleaned_data.get('username')
            user.profile.email = form.cleaned_data.get('email')
            user.profile.Profile_Picture = form.cleaned_data.get('Profile_Picture')
            user.profile.Mobile = form.cleaned_data.get('Mobile')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            messages.success(request,'Successfully Registered')
            return redirect('accounts:login')
    else:
        form = AdvertiserSignUpForm()
    return render (request, 'account/advertisersignup.html', {'form':form})

def politician_signup(request):
    if request.method=='POST':
        form = PoliticianSignUpForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.Account_type = 4
            user.profile.username = form.cleaned_data.get('username')
            user.profile.email = form.cleaned_data.get('email')
            user.profile.Profile_Picture = form.cleaned_data.get('Profile_Picture')
            user.profile.Mobile = form.cleaned_data.get('Mobile')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            messages.success(request,'Successfully Registered')
            return redirect('accounts:login')
    else:
        form = PublisherSignUpForm()
    return render (request, 'account/publishersignup.html', {'form':form})



def publisher_list(request):
    publishers = Profile.objects.filter(Account_type=1)
    context = {'publishers':publishers}
    return render(request,'publisher_list.html',context)


def add_publishers(request):
    if request.method=='POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(user)
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.Account_type = form.cleaned_data.get('Account_type')
            user.profile.username = form.cleaned_data.get('username')
            user.profile.email = form.cleaned_data.get('email')
            user.profile.Company_Name = form.cleaned_data.get('Company_Name')
            print(user.profile.Company_Name)
            user.save()
            return redirect('accounts:publisher_list')

    form = PublisherForm()
    return render(request,'add_publishers.html',{'form':PublisherForm})


def edit_publishers(request,pk):
    publisher = Profile.objects.filter(Account_type=1).get(pk=pk)
    print(publisher)
    pub_form = PublisherEditForm(instance=publisher)
    if request.method=='POST':
        form = PublisherEditForm(request.POST, instance=publisher)
        if form.is_valid():
            user = form.save()
            user.save()
            print(user)
            return redirect('accounts:publisher_list')

    form = PublisherEditForm()
    return render(request,'publisher_edit_form.html',{'form':pub_form})


def delete_publisher(request,pk):
    publisher = Profile.objects.filter(Account_type=1).get(pk=pk)
    user = User.objects.filter(username=publisher.username)
    print(publisher)
    print(user)
    publisher.delete()
    user.delete()
    return redirect('accounts:publisher_list')


def customer_list(request):
    customers = Profile.objects.filter(Account_type=2)
    context = {'customers':customers}
    return render(request,'customer_list.html',context)


def add_customers(request):
    if request.method=='POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(user)
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.Account_type = form.cleaned_data.get('Account_type')
            user.profile.username = form.cleaned_data.get('username')
            user.profile.email = form.cleaned_data.get('email')
            print(user.profile.Company_Name)
            user.save()
            return redirect('accounts:customer_list')

    form = CustomerForm()
    return render(request,'add_customers.html',{'form':CustomerForm})


def edit_customers(request,pk):
    customer = Profile.objects.filter(Account_type=2).get(pk=pk)
    print(customer)
    cus_form = CustomerEditForm(instance=customer)
    if request.method=='POST':
        form = CustomerEditForm(request.POST, instance=customer)
        if form.is_valid():
            user = form.save()
            user.save()
            print(user)
            return redirect('accounts:customer_list')

    form = CustomerEditForm()
    return render(request,'customer_edit_form.html',{'form':cus_form})

def delete_customer(request,pk):
    customer = Profile.objects.filter(Account_type=2).get(pk=pk)
    user = User.objects.filter(username=customer.username)
    customer.delete()
    user.delete()
    return redirect('accounts:customer_list')



def advertiser_list(request):
    advertisers = Profile.objects.filter(Account_type=3)
    context = {'advertisers':advertisers}
    return render(request,'advertiser_list.html',context)


def add_advertisers(request):
    if request.method=='POST':
        form = AdvertiserForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(user)
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.Account_type = form.cleaned_data.get('Account_type')
            user.profile.username = form.cleaned_data.get('username')
            user.profile.email = form.cleaned_data.get('email')
            print(user.profile.Company_Name)
            user.save()
            return redirect('accounts:advertiser_list')

    form = AdvertiserForm()
    return render(request,'add_advertisers.html',{'form':AdvertiserForm})


def edit_advertisers(request,pk):
    advertiser = Profile.objects.filter(Account_type=3).get(pk=pk)
    print(advertiser)
    adv_form = AdvertiserEditForm(instance=advertiser)
    if request.method=='POST':
        form = AdvertiserEditForm(request.POST, instance=advertiser)
        if form.is_valid():
            user = form.save()
            user.save()
            print(user)
            return redirect('accounts:advertiser_list')

    form = AdvertiserEditForm()
    return render(request,'advertiser_edit_form.html',{'form':adv_form})


def delete_advertiser(request,pk):
    advertiser = Profile.objects.filter(Account_type=3).get(pk=pk)
    user = User.objects.filter(username=advertiser.username)
    advertiser.delete()
    user.delete()
    return redirect('accounts:advertiser_list')



@login_required
def post(request):
    if request.method=='POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            print(request.user)
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            user = request.user
            print(post.user)
            print(post.State)
            # pdf = post.Add_PDF
            # print(sys.getsizeof(pdf))
            # writer = PyPDF2.PdfFileWriter()

            # for pdf in pdf:
            #     reader = PyPDF2.PdfFileReader(pdf)
            #     for i in xrange(reader.numPages):
            #         page = reader.getPage(i)
            #         page.compressContentStreams()
            #         writer.addPage(page)
            # compressed_pdf = zlib.compress(pdf,9)
            # print(sys.getsizeof(pdf))
            #compressed_pdf = os.system("ps2pdf -dPDFSETTINGS=/ebook %s reduc/%s" % (pdf,pdf))
            name = form.cleaned_data.get('Publishing_Name')
            image = post.Add_Logo
            url = post.Add_PDF.url
            newspap = NewsPaper.objects.filter(name=name)
            print(newspap)
            newspap.delete()
            newspaper = NewsPaper.objects.create(name=name,image=image,url=url)
            messages.success(request,'Post has been Uploaded')


    form = PostForm()
    return render(request,'post.html',{'form':form})



# class pdf(TemplateView):
#     template_name = 'pdf.html'

#     def get_context_data(self, **kwargs): # new
#         context = super().get_context_data(**kwargs)
#         context['key'] = 'pk_test_GHTiTTmRBwJ5c9ooU2TLvBmA'
#         return context

def newspapers(request):
    newspapers = NewsPaper.objects.all()
    print(newspapers)
    context = {'newspapers':newspapers}
    return render(request,'pdf.html',context)

def pdf(request,pk):
    newspapers = NewsPaper.objects.get(pk=pk)
    name = newspapers.name
    url = newspapers.url
    edition = newspapers.subedition
    print(name)
    print(url)
    publish_key = settings.STRIPE_PUBLISHABLE_KEY
    print(publish_key)
    context = {'name':name,'url':url,'edition':edition,'publish_key':publish_key}
    return render(request,'pdf.html',context)

def view_post(request):
    if request.user.is_superuser:
        posts = Post.objects.all()
        context = {'posts':posts}
        return render(request,'post_list.html',context)

    else :
        posts = Post.objects.filter(user = request.user)
        context = {'posts':posts}
        return render(request,'view_post.html',context)


def delete_post(request,pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('accounts:view_post')


def pubprofile(request):
    profile = Profile.objects.filter(user = request.user)
    context = {'profile':profile}
    return render(request,'publisherprofile.html',context)


@login_required
def magazine(request):
    if request.method=='POST':
        form = MagazineForm(request.POST,request.FILES)
        if form.is_valid():
            print(request.user)
            magazine = form.save(commit=False)
            print(magazine)
            user = request.user
            magazine.user = user
            magazine.save()
            print(magazine.user)
            print(magazine.Category)
            name = form.cleaned_data.get('Magazine_Name')
            image = magazine.Add_Thumbnail
            print(image)
            url = magazine.Add_Magazine.url
            print(url)
            language = form.cleaned_data.get('Language')
            category = form.cleaned_data.get('Category')
            magaz = Magazine.objects.filter(name=name)
            print(magaz)
            magaz.delete()
            mag = Magazine.objects.create(name=name,image=image,url=url,language=language,category=category)
            messages.success(request,'Magazine has been Uploaded')


    form = MagazineForm()
    return render(request,'upload_magazine.html',{'form':form})    


def articlesuploaded(request):
    if request.user.is_superuser:
        art = Article_upload.objects.all()
        context = {'articles':art}
        return render(request,'articlesuploaded.html',context)


def uploadarticlestowebsite(request,pk):
    art = Article_upload.objects.get(pk=pk)
    article = Article.objects.all()
    title = art.title
    description = art.description
    image = art.image
    if art.url:
        url = art.url
    else:
        url = ""    
    author = art.Author
    a = Article.objects.create(title=title,image=image,description=description,url=url,author=author)
    a.save()
    article = Article.objects.all()
    messages.success(request,'Article has Successfully Uploaded to Website')
    return redirect('accounts:articlesuploaded')        

def deletearticle(request,pk):
    if request.user.is_superuser:
        art = Article_upload.objects.get(pk=pk)
        art.delete()
        messages.success(request,'Successfully Deleted')
        return redirect('accounts:articlesuploaded')
     

def editprofile(request,pk):
    profile = Profile.objects.get(pk=pk)
    print(profile)
    profile_form = ProfileEditForm(instance=profile)
    if request.method=='POST':
        form = ProfileEditForm(request.POST,request.FILES, instance=profile)
        if form.is_valid():
            user = form.save()
            user.save()
            print(user)
            messages.success(request,'Successfully Updated')
            return redirect('dashboard')

    form = ProfileEditForm()
    return render(request,'profile_edit_form.html',{'form':profile_form,'p':profile})
