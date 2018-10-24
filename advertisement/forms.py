from django import forms
from .models import CreateAd,Banner
from contents.models import NewsPaper,Edition,PublisherDetail

class CreateAdForm(forms.ModelForm):
	Date = forms.DateField(widget = forms.SelectDateWidget)
	class Meta:
		model = CreateAd
		fields = '__all__'
		exclude = ('user',)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['edition'].queryset = Edition.objects.none()

		if 'edition' in self.data:
			try:
				Name_id = int(self.data.get('Name'))
				a = PublisherDetail.objects.filter(id=Name_id)
				self.fields['edition'].queryset = PublisherDetail.objects.get(id=Name_id).Sub_Edition.all()
			except (ValueError, TypeError):
				pass 
		elif self.instance.pk:
			self.fields['edition'].queryset = self.instance.PublisherDetail.Edition_set
	

class BannerForm(forms.ModelForm):
	class Meta:
		model = Banner
		fields = '__all__'
		exclude = ('user','status')
