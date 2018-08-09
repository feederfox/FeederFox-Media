from django import forms

class ContactForm(forms.Form):
	Name = forms.CharField(max_length=100)
	Email = forms.EmailField()
	Mobile = forms.IntegerField()
	Feedback = forms.CharField(widget=forms.Textarea)