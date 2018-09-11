from django import forms
from .models import PublisherDetail,Article,State,Main_Edition,Edition,State
from accounts.models import Post

class PublisherDetailsForm(forms.ModelForm):
	class Meta:
		model = PublisherDetail
		fields = '__all__'
		exclude = ('user',)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['Main_Edition'].queryset = Main_Edition.objects.none()

		if 'Main_Edition' in self.data:
			try:
				State_id = int(self.data.get('State'))
				self.fields['Main_Edition'].queryset = Main_Edition.objects.filter(State_id=State_id)
			except (ValueError, TypeError):
				pass  # invalid input from the client; ignore and fallback to empty City queryset
		elif self.instance.pk:
			self.fields['Main_Edition'].queryset = self.instance.State.Main_edition_set
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['Sub_Edition'].queryset = Edition.objects.none()

		if 'Sub_Edition' in self.data:
			try:
				State_id = int(self.data.get('State'))
				self.fields['Sub_Edition'].queryset = Edition.objects.filter(State_id=State_id)
			except (ValueError, TypeError):
				pass  # invalid input from the client; ignore and fallback to empty City queryset
		elif self.instance.pk:
			self.fields['Sub_Edition'].queryset = self.instance.State.Sub_Edition

class PublisherDetailEditForm(forms.ModelForm):
	class Meta:
		model = PublisherDetail
		fields = '__all__'
		exclude = ('user',)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['Main_Edition'].queryset = Main_Edition.objects.none()

		if 'Main_Edition' in self.data:
			try:
				State_id = int(self.data.get('State'))
				self.fields['Main_Edition'].queryset = Main_Edition.objects.filter(State_id=State_id)
			except (ValueError, TypeError):
				pass  # invalid input from the client; ignore and fallback to empty City queryset
		elif self.instance.pk:
			pass
			#self.fields['Main_Edition'].queryset = self.instance.State.Main_edition_set
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['Sub_Edition'].queryset = Edition.objects.all()

		if 'Sub_Edition' in self.data:
			try:
				State_id = int(self.data.get('State'))
				self.fields['Sub_Edition'].queryset = Edition.objects.filter(State_id=State_id)
			except (ValueError, TypeError):
				pass  # invalid input from the client; ignore and fallback to empty City queryset
		elif self.instance.pk:
			pass
			#self.fields['Sub_Edition'].queryset = self.instance.State.Sub_Edition


class ArticleForm(forms.ModelForm):
	description = forms.CharField(widget=forms.Textarea)
	class Meta:
		model = Article
		fields = '__all__'


class UploadContentForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('Type','Add_PDF','Periodicity','Number_of_Editions','Sub_Editions','Uploading_By')
		

class MainEditionForm(forms.ModelForm):
	class Meta:
		model = Main_Edition
		fields = '__all__'

class EditionForm(forms.ModelForm):
	class Meta:
		model = Edition
		fields = '__all__'				

class StateForm(forms.ModelForm):
	class Meta:
		model = State
		fields = '__all__'		