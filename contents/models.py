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

class NewsPaper(models.Model):
	name = models.CharField(max_length=100)
	url = models.URLField(null=True)
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
	name = models.CharField(max_length=100)
	url = models.URLField()
	image = models.ImageField(upload_to='Articles/',blank=True,null=True)

	def __str__(self):
		return str(self.name)
