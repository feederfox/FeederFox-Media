from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

ACCCOUNT_TYPES_CHOICES = [
	('1','Publisher'),
	('2','Customer'),
	('3','Advertiser')
]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    Account_type = models.CharField(max_length=100,choices=ACCCOUNT_TYPES_CHOICES)
    Company_Name = models.CharField(max_length=100,blank=True,null=True)
    Firstname = models.CharField(max_length=100,blank=True,null=True)
    Lastname = models.CharField(max_length=100,blank=True,null=True)
    Address = models.CharField(max_length=1000,blank=True,null=True)
    Mobile = models.CharField(max_length=100,blank=True,null=True)


    def __str__(self):
        return str(self.user)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()		

# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# post_save.connect(create_user_profile, sender=User)

PERIODICITY_CHOICES = [
    ('Daily', 'Daily'),
    ('Weekly', 'Weekly'),
    ('Monthly', 'Monthly'),
    ('Yearly', 'Yearly'),
    ]

UPLOADING_CHOICES = [
        ('Single_File','Single_File'),
        ('Page_by_Page','Page_by_Page'),
        ('Edition','Edition'),
        ('Api_code','Api_code'),
]    



class Post(models.Model):
    Publishing_House = models.CharField(max_length=100)
    Publishing_Name = models.CharField(max_length=100)
    Add_Logo = models.FileField(upload_to='media/')
    Number_of_Editions = models.PositiveIntegerField()
    Sub_Editions = models.CharField(max_length=100)
    Place = models.CharField(max_length=400)
    Languages = models.CharField(max_length=100)
    Periodicity = models.CharField(max_length=100,choices=PERIODICITY_CHOICES,default='Daily')
    Uploading_By = models.CharField(max_length=100,choices=UPLOADING_CHOICES,default='Single_File')
    Uploader_Contact_Details = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.Publishing_Name)