from django.db import models

class NationalNewsChannel(models.Model):
	channel_name = models.CharField(max_length=100)
	channel_url = models.URLField()
	channel_image = models.ImageField(blank=True,null=True)

	def __str__(self):
		return str(self.channel_name)

class RegionalNewsChannel(models.Model):			
	channel_name = models.CharField(max_length=100)
	channel_url = models.URLField()
	channel_image = models.ImageField(blank=True,null=True)

	def __str__(self):
		return str(self.channel_name)


# class NewsChannel(models.Model):
# 	National = models.ForeignKey(NationalNewsChannel,on_delete=models.CASCADE)
# 	Regional = models.ForeignKey(RegionalNewsChannel,on_delete=models.CASCADE)



class NationalNewsPaper(models.Model):
	newspaper_name = models.CharField(max_length=100)
	newspaper_url = models.URLField()
	newspaper_image = models.ImageField(blank=True,null=True)

	def __str__(self):
		return str(self.newspaper_name)


class RegionalNewsPaper(models.Model):
	newspaper_name = models.CharField(max_length=100)
	newspaper_url = models.URLField()
	newspaper_image = models.ImageField(blank=True,null=True)

	def __str__(self):
		return str(self.newspaper_name)


class Magazine(models.Model):
	magazine_name = models.CharField(max_length=100)
	magazine_url = models.URLField()
	magazine_image = models.ImageField(blank=True,null=True)

	def __str__(self):
		return str(self.magazine_name)

class SocialChannel(models.Model):
	socialchannels_name = models.CharField(max_length=100)
	socialchannels_url = models.URLField()
	socialchannels_image = models.ImageField(blank=True,null=True)

	def __str__(self):
		return str(self.socialchannels_name)

class Ebook(models.Model):
	ebooks_name = models.CharField(max_length=100)
	ebooks_url = models.URLField()
	ebooks_image = models.ImageField(blank=True,null=True)

	def __str__(self):
		return str(self.ebooks_name)		
