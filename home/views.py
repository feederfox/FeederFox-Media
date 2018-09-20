import os
from django.conf import settings

from django.contrib.auth import login, authenticate
import datetime
from django.shortcuts import render, redirect
from django.views.generic import TemplateView  # Import TemplateView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.models import Profile
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.template.loader import get_template
from contents.models import NewsPaper,Magazine,PublisherDetail,PoliticalForum,Article


# Add the two views we have been talking about  all this time :)
def regionalnewspaper(request):
    return render(request,'regionalnewspaper.html',{})

def admin(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return render(request,'admin_dashboard.html',{})
        messages.error(request,'Please Login with Admin Credentials')
    return redirect('accounts:admin_login')


@login_required
def dashboard(request):

    if request.user.is_superuser:
        return render(request,'admin_dashboard.html',{})
    messages.error(request,'Please Login with Admin Credentials')
    if request.user.profile.Account_type=='1':
        print(request.user.profile.Account_type)
        return render (request,'publisher_dashboard.html',{})
    elif request.user.profile.Account_type=='2':
        return render(request,'customer_dashboard.html',{})
    elif request.user.profile.Account_type=='3':    
        return render(request,'advertiser_dashboard.html',{})
    return render(request,'politiciandashboard.html',{})    

def article1(request):
    return render(request,'article1.html',{})

def article2(request):
    return render(request,'article2.html',{})

def article3(request):
    return render(request,'article3.html',{})

def article4(request):
    return render(request,'article4.html',{})

def contact(request):
    form = ContactForm()
    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            Name = request.POST.get('Name')
            Email = request.POST.get('Email')
            Mobile = request.POST.get('Mobile')
            Feedback = request.POST.get('Feedback')
            template = get_template('contact_template.txt')
            context = {
                'contact_name': Name,
                'contact_email': Email,
                'contact_mobile': Mobile,
                'contact_feedback':Feedback
            }
            content = template.render(context)
            email = EmailMessage(
                "New contact form submission",
                content,
                "feederfox.com" +'',
                ['contactus.feederfox@gmail.com'],
                headers = {'Reply-To': Email }
            )
            email.send()
            return redirect('contact')

    return render(request,'contact.html',{'form':form})

def index(request):
    newspaper = NewsPaper.objects.all()
    print(newspaper)
    nam = []
    for i in newspaper:
        nam.append(i)
    print(nam)    
    name = nam
    print(name)
    magazine = Magazine.objects.all()
    pub = PublisherDetail.objects.all()
    political = PoliticalForum.objects.all()
    pubdetails = PublisherDetail.objects.filter(Name__in=name)
    articles = Article.objects.all()
    print(political)
    context = {'newspapers':newspaper,'magazines':magazine,'pubdetails':pubdetails,'articles':articles,'political':political}
    return render(request,'index.html',context)

# class HomePageView(TemplateView):
#     template_name = "index.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

class FaqPageView(TemplateView):
    template_name = "faq.html"

class PrivacyPageView(TemplateView):
    template_name = "privacy.html"


def publisherpage(request):
    return render(request,'publisher_page.html',{})

def customerpage(request):
    return render(request,'customer_page.html',{})

def advertiserpage(request):
    return render(request,'advertiser_page.html',{})

def video1(request):
    return render(request,'video1.html',{})

def video2(request):
    return render(request,'video2.html',{})

def video3(request):
    return render(request,'video3.html',{})

def video4(request):
    return render(request,'video4.html',{})

def video5(request):
    return render(request,'video5.html',{})

def video6(request):
    return render(request,'video6.html',{})


def video7(request):
    return render(request,'video7.html',{})
