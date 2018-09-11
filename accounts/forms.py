
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Post,Magazines
from contents.models import State

ACCCOUNT_TYPES_CHOICES = [
	('1','Publisher'),
	('2','Customer'),
	('3','Advertiser')
]

PUBLISHER_CHOICES = [
	('1','Publisher')
]

CUSTOMER_CHOICES = [
	('2','Customer')
]

ADVERTISER_CHOICES = [
	('3','Advertiser')
]

class SignUpForm(UserCreationForm):
	email = forms.EmailField()
	Account_type = forms.ChoiceField(choices = ACCCOUNT_TYPES_CHOICES)
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2','Account_type' )

class PublisherSignUpForm(UserCreationForm):
	email = forms.EmailField()
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')

	def clean_email(self):
		email = self.cleaned_data.get('email')
		username = self.cleaned_data.get('username')
		print (User.objects.filter(email=email).count())
		if email and User.objects.filter(email=email).count() > 0:
			raise forms.ValidationError(u'This email address is already registered.')
		return email

class AdvertiserSignUpForm(UserCreationForm):
	email = forms.EmailField()
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')

	def clean_email(self):
		email = self.cleaned_data.get('email')
		username = self.cleaned_data.get('username')
		print (User.objects.filter(email=email).count())
		if email and User.objects.filter(email=email).count() > 0:
			raise forms.ValidationError(u'This email address is already registered.')
		return email

class CustomerSignUpForm(UserCreationForm):
	email = forms.EmailField()
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')

	def clean_email(self):
		email = self.cleaned_data.get('email')
		username = self.cleaned_data.get('username')
		print (User.objects.filter(email=email).count())
		if email and User.objects.filter(email=email).count() > 0:
			raise forms.ValidationError(u'This email address is already registered.')
		return email
class PostForm(forms.ModelForm):
	# State = forms.ModelChoiceField(queryset=State.objects.all(),empty_label="Select State")

	class Meta:
		model = Post
		fields = ('Publishing_House','Publishing_Name','Add_PDF','Add_Logo','Type','Number_of_Editions','Sub_Editions','State','Languages','Periodicity',
			'Uploading_By')

class PublisherForm(UserCreationForm):
	email = forms.EmailField()
	Account_type = forms.ChoiceField(choices = PUBLISHER_CHOICES)
	Company_Name = forms.CharField(max_length=100)
	class Meta:
		model = User
		fields = ('username','email','password1','password2','Account_type','Company_Name')

class PublisherEditForm(forms.ModelForm):
	email = forms.EmailField()
	Company_Name = forms.CharField(max_length=100)
	Firstname = forms.CharField(max_length=100)
	Lastname = forms.CharField(max_length=100)
	Mobile = forms.CharField(max_length=100)
	Address = forms.CharField(max_length=1000)
	class Meta:
		model = User
		fields = ('email','Firstname','Lastname','Company_Name','Mobile','Address')

class CustomerForm(UserCreationForm):
	email = forms.EmailField()
	Account_type = forms.ChoiceField(choices = CUSTOMER_CHOICES)
	class Meta:
		model = User
		fields = ('username','email','password1','password2','Account_type')

class CustomerEditForm(forms.ModelForm):
	email = forms.EmailField()
	Firstname = forms.CharField(max_length=100)
	Lastname = forms.CharField(max_length=100)
	Mobile = forms.CharField(max_length=100)
	Address = forms.CharField(max_length=1000)
	class Meta:
		model = User
		fields = ('email','Firstname','Lastname','Mobile','Address')

class AdvertiserForm(UserCreationForm):
	email = forms.EmailField()
	Account_type = forms.ChoiceField(choices = ADVERTISER_CHOICES)
	class Meta:
		model = User
		fields = ('username','email','password1','password2','Account_type')

class AdvertiserEditForm(forms.ModelForm):
	email = forms.EmailField()
	Firstname = forms.CharField(max_length=100)
	Lastname = forms.CharField(max_length=100)
	Mobile = forms.CharField(max_length=100)
	Address = forms.CharField(max_length=1000)
	class Meta:
		model = User
		fields = ('email','Firstname','Lastname','Mobile','Address')

class MagazineForm(forms.ModelForm):
	class Meta:
		model = Magazines
		fields = ('Publishing_House','Magazine_Name','Add_Thumbnail','Add_Magazine','Language','Category','Periodicity','Place')