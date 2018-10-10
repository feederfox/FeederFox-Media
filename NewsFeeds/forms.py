from django import forms
from .models import Newsfeeds

class NewsfeedsForm(forms.ModelForm):
	class Meta:
		model = Newsfeeds
		fields = '__all__'
