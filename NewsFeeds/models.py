from django.db import models

# Create your models here..
NEWSFEEDS_CHOICES=[
('1','Headlines'),
('2','Educational'),
('3','Entertainment'),
('4','Business'),
('5','Sports'),
('6','Lifestyles'),
('7','Social'),
('8','World'),
('9','Global'),
]



class Newsfeeds(models.Model):
	
	image = models.ImageField(upload_to='newsfeeds')
	title = models.CharField(max_length=100)
	category = models.CharField(max_length=100,choices=NEWSFEEDS_CHOICES)
	description = models.CharField(max_length=800)

	def __str__(self):
		return str(self.title)