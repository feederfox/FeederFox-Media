from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Post

ACCCOUNT_TYPES_CHOICES = [
	('1','Publisher'),
	('2','Customer'),
	('3','Advertiser')
]

class SignUpForm(UserCreationForm):
	email = forms.EmailField()
	Account_type = forms.ChoiceField(choices = ACCCOUNT_TYPES_CHOICES)
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2','Account_type' )

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = '__all__'
