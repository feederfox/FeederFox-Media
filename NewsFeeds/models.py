from django.db import models

# Create your models here..
NEWSFEEDS_CHOICES=[
('Headlines','Headlines'),
('Educational','Educational'),
('Entertainment','Entertainment'),
('Business','Business'),
('Sports','Sports'),
('Lifestyles','Lifestyles'),
('Social','Social'),
('World','World'),
('Global','Global'),
]



class Newsfeeds(models.Model):
	
	image = models.ImageField(upload_to='newsfeeds')
	title = models.CharField(max_length=100)
	category = models.CharField(max_length=100,choices=NEWSFEEDS_CHOICES)
	description = models.CharField(max_length=800)

	def __str__(self):
		return str(self.title)