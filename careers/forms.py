from django import forms
from .models import Current_Openings,Applications

class CurrentOpeningsForm(forms.ModelForm):
	class Meta:
		model = Current_Openings
		fields = '__all__'
		exclude = ('user',)

class ApplicationsForm(forms.ModelForm):
	class Meta:
		model = Applications
		fields = '__all__'
		exclude = ('user','Position',)		