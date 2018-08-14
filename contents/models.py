from django.db import models

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
	image = models.ImageField(blank=True,null=True)

	def __str__(self):
		return str(self.name)

class SocialChannel(models.Model):
	name = models.CharField(max_length=100)
	url = models.URLField()
	image = models.ImageField(blank=True,null=True)

	def __str__(self):
		return str(self.name)

class Ebook(models.Model):
	name = models.CharField(max_length=100)
	url = models.URLField()
	image = models.ImageField(blank=True,null=True)

	def __str__(self):
		return str(self.name)		
