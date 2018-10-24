from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.template.loader import get_template
from .forms import CurrentOpeningsForm,ApplicationsForm
from .models import Current_Openings,Applications

@login_required
def postopenings(request):
	if request.method =='POST':
		form = CurrentOpeningsForm(request.POST)
		if form.is_valid():
			a = form.save(commit = False)
			a.user = request.user
			a.save()
			messages.success(request,'Successfully Posted')

	form = CurrentOpeningsForm()
	return render(request,'careers/postopenings.html',{'form':form})		


def viewopenings(request):
	openings = Current_Openings.objects.all()
	return render(request,'careers.html',{'openings':openings})

@login_required(login_url='/accounts/login/')
def application(request,pk):
	position = Current_Openings.objects.get(pk=pk)
	print(position)
	if request.method =='POST':
		form = ApplicationsForm(request.POST,request.FILES)
		if form.is_valid():
			a = form.save(commit = False)
			a.user = request.user
			print(a.user)
			a.Position = position
			a.save()
			print(a)
			Position = a.Position
			Name = a.Name
			Experience = a.Experience
			Email = a.Email
			Mobile = a.Mobile
			Feedback = a.Feedback
			Resume = request.FILES['Resume']
			template = get_template('application.txt')
			context = {
            	'Position':Position,
                'contact_name': Name,
                'Experience': Experience,
                'contact_email': Email,
                'contact_mobile': Mobile,
                'contact_feedback':Feedback
            }
			content = template.render(context)
			email = EmailMessage(
                "New Job Application",
                content,
                "feederfox.com" +'',
                ['sameer.feederfox@gmail.com'],
                headers = {'Reply-To': Email }
            )
			email.attach(Resume.name, Resume.read(), Resume.content_type)
			email.send()
			messages.success(request,'Successfully Applied')
			return redirect('careers:viewopenings')

	form = ApplicationsForm()
	return render(request,'applicationform.html',{'form':form})	