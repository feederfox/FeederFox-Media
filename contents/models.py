from django.db import models
from django_mysql.models import ListCharField
from django.db.models import CharField
from django.contrib.auth.models import User

CONTENT_CHOICES = [
		('1','Paper'),
		('2','Magazine'),
]

class State(models.Model):
	name = models.CharField(max_length=100)
	image = models.ImageField(upload_to='States/',blank=True,null=True)

	def __str__(self):
		return str(self.name)

class NationalNewsChannel(models.Model):
	name = models.CharField(max_length=100)
	url = models.URLField()
	image = models.ImageField(blank=True,null=True)

	def __str__(self):
		return str(self.name)

class RegionalNewsChannel(models.Model):
	name = models.CharField(max_length=100)
	url = models.URLField()
	image = models.ImageField(blank=True,null=True)

	def __str__(self):
		return str(self.name)

class NewsPaper(models.Model):
	name = models.CharField(max_length=100)
	url = models.URLField(null=True)
	image = models.ImageField(blank=True,null=True)
	mainedition = models.CharField(max_length=100,blank=True,null=True)
	subedition = models.CharField(max_length=100,blank=True,null=True) 
	user = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
	Uploaded_at = models.CharField(max_length=100)

	def __str__(self):
		return str(self.name)

class NationalNewsPaper(models.Model):
	name = models.CharField(max_length=100)
	url = models.URLField()
	image = models.ImageField(blank=True,null=True)

	def __str__(self):
		return str(self.name)


class RegionalNewsPaper(models.Model):
	name = models.CharField(max_length=100)
	url = models.URLField()
	image = models.ImageField(blank=True,null=True)

	def __str__(self):
		return str(self.name)


class Magazine(models.Model):
	name = models.CharField(max_length=100)
	url = models.URLField()
	image = models.ImageField(upload_to='Magazine/',blank=True,null=True)
	language = models.CharField(max_length=100,null=True)
	category = models.CharField(max_length=100,null=True)

	def __str__(self):
		return str(self.name)

class SocialChannel(models.Model):
	name = models.CharField(max_length=100)
	url = models.URLField()
	image = models.ImageField(upload_to='SocialChannel/',blank=True,null=True)

	def __str__(self):
		return str(self.name)

class Ebook(models.Model):
	name = models.CharField(max_length=100)
	url = models.URLField()
	image = models.ImageField(upload_to='Ebook/',blank=True,null=True)

	def __str__(self):
		return str(self.name)


class Article(models.Model):
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=10000)
	image = models.ImageField(upload_to='Articles/',blank=True,null=True)

	def __str__(self):
		return str(self.title)


class Main_Edition(models.Model):
	State = models.ForeignKey(State,on_delete=models.CASCADE)
	Name = models.CharField(max_length=100)

	def __str__(self):
		return str(self.Name)

class Edition(models.Model):
	State = models.ForeignKey(State,on_delete=models.CASCADE)
	Name = models.CharField(max_length=100)

	def __str__(self):
		return str(self.Name)
		
class Sub_Edition(models.Model):
	Name = models.CharField(max_length=100)
	Edition = models.CharField(max_length=100)

	def __str__(self):
		return str(self.Edition)

class PublisherDetail(models.Model):
	Name = models.CharField(max_length=100)
	Language = models.CharField(max_length=100)
	Add_Logo = models.FileField(upload_to='publisher_details/',blank=True,null=True)
	Type = models.CharField(max_length=100,choices = CONTENT_CHOICES)
	State = models.ForeignKey(State,on_delete=models.CASCADE)
	Main_Edition = models.ForeignKey(Main_Edition,on_delete=models.CASCADE,blank=True,null=True)
	Sub_Edition = models.ManyToManyField(Edition,blank=True,null=True)
	user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
	#Main_Edition = ListCharField(base_field=CharField(max_length=100),size=None,max_length=10000,blank=True,null=True)
	#Edition = ListCharField(base_field=CharField(max_length=100),size=None,max_length=10000,blank=True,null=True)

	def __str__(self):
		return str(self.Name)
