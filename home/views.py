from django.contrib.auth import login, authenticate

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



# Add the two views we have been talking about  all this time :)

def admin(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return render(request,'admin_dashboard.html',{})
        messages.error(request,'Please Login with Admin Credentials')    
    return redirect('accounts:admin_login')        
    

@login_required
def dashboard(request):
    a = User.objects.all()
    p = Profile.objects.all()
    
    return redirect('accounts:post')

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
                ['sameer.feederfox@gmail.com'],
                headers = {'Reply-To': Email }
            )
            email.send()
            return redirect('contact')

    return render(request,'contact.html',{'form':form})

class HomePageView(TemplateView):
    template_name = "index.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

class FaqPageView(TemplateView):
    template_name = "faq.html"

class PrivacyPageView(TemplateView):
    template_name = "privacy.html"



class PublisherSignupPageView(TemplateView):
    template_name = "publisher_signup.html"

    def get(self, request):
        form = HomeForm()


        return render(request, self.template_name, {'form': form})

    def post(self, request):
        sample_chapter = None
        text = None
        form = HomeForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()


            text = form.cleaned_data['post']
            sample_chapter = form.cleaned_data['post']
            form = HomeForm()
            # return redirect('home:home')

        args = {'form': form, 'text': text, 'sample_chapter': sample_chapter}
        return render(request, 'publisher_signup.html', args)

