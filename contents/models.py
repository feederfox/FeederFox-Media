from django.db import models
from django_mysql.models import ListCharField
from django.db.models import CharField
from django.contrib.auth.models import User
from vote.models import VoteModel

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
	image = models.ImageField(upload_to='Ebooks/',blank=True,null=True)

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

class PoliticalForum(VoteModel,models.Model):
	Name = models.CharField(max_length=100)
	Image = models.ImageField(upload_to='Politicians/',)
	Synopsis = models.CharField(max_length=10000)
	Projects_Taken = models.CharField(max_length=10000,blank=True,null=True)
	#Date_of_Birth = models.DateField(auto_now=False,auto_now_add=False)
	Educational_Qualification = models.CharField(max_length=100)
	Family_History = models.CharField(max_length=1000)
	video_link = models.URLField()

	def __str__(self):
		return str(self.Name)

class Dummy(models.Model):
	name = models.CharField(max_length=100)
	image = models.URLField(max_length=100)
	url = models.URLField()

	def __str__(self):
		return str(self.name)		


class Article_upload(models.Model):
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=10000)
	image = models.ImageField(upload_to='Articles/',blank=True,null=True)
	url = models.URLField(blank=True,null=True)
	Author = models.CharField(max_length=100,blank=True,null=True)

	def __str__(self):
		return str(self.title)

class Revenue(models.Model):
	MonthlyRevenue = models.CharField(max_length=50)
	Month = models.CharField(max_length=50)

	def __str__(self):
		return '%s %s' % (self.MonthlyRevenue, self.Month)		

class ArticleReview(VoteModel,models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	upvote = models.CharField(max_length=100)
	downvote = models.CharField(max_length=100)
	review = models.CharField(max_length=10000,blank=True,null=True)

	def __str__(self):
		return str(self.user)		

class Month(models.Model):
	Month_Name = models.CharField(max_length=100)

	def __str__(self):
		return str(self.Month_Name)

class PoliticianArticle(models.Model):
	Name = models.CharField(max_length=100)
	Image = models.ImageField(upload_to='Politician_Articles/',)
	Month = models.ForeignKey(Month,on_delete=models.CASCADE)
	Description = models.CharField(max_length=10000)		

	def __str__(self):
		return str(self.Name)

class Polling(models.Model):
	Name = models.CharField(max_length=100)
	Month = models.ForeignKey(Month,on_delete=models.CASCADE)
	Poll_Question = models.CharField(max_length=1000)
	Upvote = models.PositiveIntegerField(default=0)
	DownVote = models.PositiveIntegerField(default=0)		

	def __str__(self):
		return str(self.Poll_Question)

class Vote(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='vote_user')
	Poll_Question = models.CharField(max_length=1000)

	def __str__(self):
		return '%s,%s' %(self.user,self.Poll_Question)		

class PoliticalSurvey(models.Model):
	Name = models.CharField(max_length=100)
	Poll_Question = models.CharField(max_length=1000)

	def __str__(self):
		return '%s,%s' %(self.Name,self.Poll_Question)			