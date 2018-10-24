from django.db import models

class Current_Openings(models.Model):
	Position = models.CharField(max_length=250)
	Experience = models.CharField(max_length=250)
	Job_Description = models.CharField(max_length=10000)
	Roles_and_Responsibilities = models.CharField(max_length=10000)
	user = models.CharField(max_length=100)

	def __str__(self):
		return str(self.Position)

class Applications(models.Model):
	Position = models.CharField(max_length=250)
	Name = models.CharField(max_length=200)
	Experience = models.CharField(max_length=100)
	Email = models.EmailField()
	Mobile = models.PositiveIntegerField()
	Resume = models.FileField(upload_to='Resumes/')
	Feedback = models.CharField(max_length=10000)
	user = models.CharField(max_length=100)

	def __str__(self):
		return str(self.Name)