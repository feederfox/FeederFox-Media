from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from .forms import CreateAdForm,BannerForm
from .models import CreateAd,Banner
from contents.models import PublisherDetail,NewsPaper,Edition

@login_required(login_url='/accounts/login/')
def createad(request):
	if request.method == 'POST':
		form = CreateAdForm(request.POST)
		if form.is_valid():
			a = form.save(commit = False)
			a.user = request.user
			if a.Page_Num in ('1','2','3'):
				c = a.Duration * 100
			elif a.Page_Num in ('4','5','6'):
				c = a.Duration * 80
			else:
				c = a.Duration * 60		
			a.save()
			form.save_m2m()
			messages.success(request,'Successfully Created')
			return render(request,'advertisement/createad.html',{'form':form,'c':c})
		else:
			messages.error(request,'Error')
	form = CreateAdForm()
	return render(request,'advertisement/createad.html',{'form':form})		

def load_edition(request):
    Name_id = request.GET.get('Name')
    edition = PublisherDetail.objects.get(id=Name_id)
    return render(request, 'advertisement/editiondropdownlist.html', {'editions': edition})   

@login_required(login_url='/accounts/login/')
def addbanner(request):
	if request.method == 'POST':
		form = BannerForm(request.POST,request.FILES)
		if form.is_valid():
			a = form.save(commit = False)
			a.user = request.user
			a.save()
			messages.success(request,'Successfully Added')
		else:
			messages.error(request,'Error')
	form = BannerForm()
	return render(request,'advertisement/addbanner.html',{'form':form})



def viewbanner(request):
	if request.user.is_superuser:
		banner = Banner.objects.all()
		context = {'banners':banner}
		return render(request,'viewbanners_admin.html',context)

	else :
		banner = Banner.objects.filter(user = request.user)
		context = {'banners':banner}
		return render(request,'advertisement/viewbanners.html',context)	

def approvebanner(request,pk):
	if request.user.is_superuser:
		banner = Banner.objects.get(pk=pk)
		print(Banner)
		if banner.status == 0:
			banner.status+=1
		
		banner.save()
		return redirect('advertisement:viewbanner')