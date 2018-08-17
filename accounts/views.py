from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect,HttpResponse
from .forms import ( SignUpForm,PostForm,PublisherForm,PublisherEditForm,CustomerEditForm,CustomerForm,
                        AdvertiserForm,AdvertiserEditForm,PublisherSignUpForm,AdvertiserSignUpForm,CustomerSignUpForm)
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

def publisher_signup(request):
    if request.method=='POST':
        form = PublisherSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.Account_type = 1
            user.profile.username = form.cleaned_data.get('username')
            user.profile.email = form.cleaned_data.get('email')
            print(user.profile.Account_type)
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('accounts:login')
    else:
        form = PublisherSignUpForm()
    return render (request, 'account/publishersignup.html', {'form':form})    


def customer_signup(request):
    if request.method=='POST':
        form = CustomerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.Account_type = 2
            user.profile.username = form.cleaned_data.get('username')
            user.profile.email = form.cleaned_data.get('email')
            print(user.profile.Account_type)
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('accounts:login')
    else:
        form = CustomerSignUpForm()
    return render (request, 'account/signup.html', {'form':form})    



def advertiser_signup(request):
    if request.method=='POST':
        form = AdvertiserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.Account_type = 3
            user.profile.username = form.cleaned_data.get('username')
            user.profile.email = form.cleaned_data.get('email')
            print(user.profile.Account_type)
            user.save()

            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('accounts:login')
    else:
        form = AdvertiserSignUpForm()
    return render (request, 'account/advertisersignup.html', {'form':form})    


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
            form.save()
            Uploader_Contact_Details = request.user
            print(Uploader_Contact_Details)
            messages.success(request,'Post has been Uploaded')

    form = PostForm()        
    return render(request,'post.html',{'form':form})    


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
