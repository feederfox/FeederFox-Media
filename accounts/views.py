from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect,HttpResponse
from .forms import SignUpForm,PostForm
from .models import Profile,Post
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

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
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('accounts:login')
    else:
        form = SignUpForm()
    return render(request, 'account/signup.html', {'form': form})



def publisher_list(request):
	publishers = Profile.objects.filter(Account_type=1)
	print(publishers)
	context = {'publishers':publishers}
	return render(request,'publisher_list.html',context) 

def customer_list(request):
	customers = Profile.objects.filter(Account_type=2)
	context = {'customers':customers}
	return render(request,'customer_list.html',context) 

def advertiser_list(request):
	advertisers = Profile.objects.filter(Account_type=3)
	context = {'advertisers':advertisers}
	return render(request,'advertiser_list.html',context) 


@login_required
def post(request):
    form = PostForm()
    if request.method=='POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Post has been Uploaded')

    return render(request,'post.html',{'form':form})    
