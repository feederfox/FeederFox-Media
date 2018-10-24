from django.db import models

from contents.models import NewsPaper,Edition,PublisherDetail

PAGE_CHOICES = [('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10'),]

class CreateAd(models.Model):
	Name = models.ForeignKey(PublisherDetail,on_delete = models.CASCADE)
	edition = models.ForeignKey(Edition,on_delete=models.CASCADE,related_name = 'Edition')
	Page_Num = models.CharField(max_length = 100,choices = PAGE_CHOICES)
	Date = models.DateField(auto_now = False,auto_now_add = False)
	Duration = models.PositiveIntegerField()
	user = models.CharField(max_length=200)

	def __str__(self):
		return str(self.Name)

class Banner(models.Model):
	Name = models.CharField(max_length=222)
	Banner_Link = models.URLField(blank=True,null=True)
	Banner_Image = models.ImageField(upload_to = 'Advertisements/')
	user = models.CharField(max_length=220)
	status  = models.PositiveIntegerField(default = '0')

	def __str__(self):
		return str(self.Name)