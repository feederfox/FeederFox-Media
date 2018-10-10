from django import forms
from .models import NewsFeed

class NewsFeedsForm(forms.ModelForm):
	class Meta:
		model = NewsFeed
		fields = '__all__'