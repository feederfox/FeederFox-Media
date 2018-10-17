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
from contents.models import NewsPaper,Magazine,PublisherDetail,PoliticalForum,Article,EbookUpload
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from social_django.models import UserSocialAuth
import json
from django.views.decorators.csrf import csrf_exempt
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer




# Add the two views we have been talking about  all this time :)
def regionalnewspaper(request):
    return render(request,'regionalnewspaper.html',{})

def admin(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return render(request,'admin_dashboard.html',{})
    return redirect('accounts:admin_login')


@login_required
def dashboard(request):
    a = request.user
    print(a)
    p = Profile.objects.get(username=a)
    print(p)
    if request.user.is_superuser:
        return render(request,'admin_dashboard.html',{})
    messages.error(request,'Please Login with Admin Credentials')
    if request.user.profile.Account_type=='1':
        print(request.user.profile.Account_type)
        return render (request,'publisher_dashboard.html',{'p':p})
    elif request.user.profile.Account_type=='2':
        return render(request,'customer_dashboard.html',{'p':p})
    elif request.user.profile.Account_type=='3':    
        return render(request,'advertiser_dashboard.html',{'p':p})
    return render(request,'politiciandashboard.html',{'p':p})    

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
    ebook = EbookUpload.objects.all()
    political = PoliticalForum.objects.all()
    pubdetails = PublisherDetail.objects.filter(Name__in=name)
    print(pubdetails)
    a = int((len(pubdetails))/2)
    pub1 = PublisherDetail.objects.filter(Name__in=name)[:a]
    pub2 = PublisherDetail.objects.filter(Name__in=name)[a:]
    print(pub1)
    print(len(pubdetails))
    print((len(pubdetails))/2)
    articles = Article.objects.all().reverse()
    print(political)
    title = "Chatbot Version 1.0"
    context = {'newspapers':newspaper,'magazines':magazine,'pubdetails':pubdetails,'articles':articles,
            'political':political,'ebook':ebook,'title':title,'pub1':pub1,'pub2':pub2}
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

@login_required
def settings(request):
    user = request.user

    try:
        github_login = user.social_auth.get(provider='github')
    except UserSocialAuth.DoesNotExist:
        github_login = None

    try:
        twitter_login = user.social_auth.get(provider='twitter')
    except UserSocialAuth.DoesNotExist:
        twitter_login = None

    try:
        facebook_login = user.social_auth.get(provider='facebook')
    except UserSocialAuth.DoesNotExist:
        facebook_login = None

    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

    return render(request, 'settings.html', {
        'github_login': github_login,
        'twitter_login': twitter_login,
        'facebook_login': facebook_login,
        'can_disconnect': can_disconnect
    })

@login_required
def password(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordForm(request.user)
    return render(request, 'password.html', {'form': form})


@csrf_exempt
def get_response(request):
	bot = Chatbot('Bot')
	chatbot = ChatBot(
    'Bot',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
	)
# Train based on the english corpus
	chatbot.train("chatterbot.corpus.english")
	#bot.set_trainer(ListTrainer)
	response = {'status': None}
	if request.method == 'POST':
		data = json.loads(request.body)
		message = data['message']
		chat_response = chatbot.get_response(message).text
		response['message'] = {'text': chat_response, 'user': False, 'chat_bot': True}
		response['status'] = 'ok'
	else:
		response['error'] = 'no post data found'
		return HttpResponse(
			json.dumps(response),
			content_type="application/json"
			)



def comingSoon(request):
    return render(request,'coming-soon.html',{})

def articlePage(request):
    articles = Article.objects.all()
    context = {'articles':articles}
    return render(request,'all_article.html',context)

def consultingpage(request):
    return render(request,'consulting.html',{})

def ebooksviewall(request):
    ebook = EbookUpload.objects.all()
    context = {'ebook':ebook}
    return render(request,'ebooksviewall.html',context)

def careers1(request):
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
            print(context)
            print(content)
            email = EmailMessage(
                "New contact form submission",
                content,
                "feederfox.com" +'',
                ['vinaytm7@gmail.com'],
                headers = {'Reply-To': Email }
            )
            email.send()
            return redirect('careers1')

    return render(request,'careers.html',{'form':form})

    