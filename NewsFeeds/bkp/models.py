from django.db import models

CATEGORY_CHOICES = [
	('1','Headlines/Breaking News'),
	('2','Education'),
	('3','Entertainment'),
	('4','Business'),
	('5','Sports'),
	('6','LifeStyle'),
	('7','Social'),
	('8','World/International'),
	('9','Global'),
]

class NewsFeed(models.Model):
	title = models.CharField(max_length=250)
	description = models.CharField(max_length=10000)
	image = models.ImageField(upload_to = 'NewsFeeds/')
	category = models.CharField(max_length = 100,choices = CATEGORY_CHOICES)
	created_at = models.DateField(auto_now=True,auto_now_add=False)

	def __str__(self):
		return str(self.title)
