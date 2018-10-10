from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from contents.models import State,PublisherDetail,Sub_Edition

ACCCOUNT_TYPES_CHOICES = [
    ('1','Publisher'),
    ('2','Customer'),
    ('3','Advertiser'),
    ('4','Politician')
]

ACCOUNT_CHOICES = [
    ('1','Android'),
    ('2','IOS'),
]


LOGIN_CHOICES = [
    ('0','Normal'),
    ('1','Facebook'),
    ('2','GooglePlus'),
]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE,null=True)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    Account_type = models.CharField(max_length=100,choices=ACCCOUNT_TYPES_CHOICES)
    Company_Name = models.CharField(max_length=100,blank=True,null=True)
    Firstname = models.CharField(max_length=100,blank=True,null=True)
    Lastname = models.CharField(max_length=100,blank=True,null=True)
    Address = models.CharField(max_length=1000,blank=True,null=True)
    Mobile = models.IntegerField(blank=True,null=True)
    password1 = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)
    Application_type = models.CharField(max_length=100,choices=ACCOUNT_CHOICES,null=True)
    Profile_Picture = models.ImageField(upload_to='Profiles/',blank=True,null=True)
    Social_login = models.CharField(max_length=100,choices=LOGIN_CHOICES,null=True)

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

TYPE_CHOICES = [
        ('1','National'),
        ('2','Regional'),
]

TYPE_CHOICES = [
        ('1','National'),
        ('2','Regional'),
]


CATEGORY_CHOICES = [
        ('1','Entertainment'),
        ('2','Sports'),
        ('3','Health'),
        ('4','Business'),
]

class Post(models.Model):
    Publishing_House = models.CharField(max_length=100)
    Publishing_Name = models.CharField(max_length=100)
    Add_PDF = models.FileField(upload_to='NewsPapers/',null=True)
    Add_Logo = models.FileField(upload_to='Logos/',null=True)
    Number_of_Editions = models.PositiveIntegerField()
    Main_Edition = models.CharField(max_length=100,blank=True,null=True)
    Sub_Editions = models.ForeignKey(Sub_Edition,on_delete=models.SET_NULL,blank=True,null=True)
    Sub_Edition = models.CharField(max_length=100)
    State = models.ForeignKey(State,on_delete=models.CASCADE,null=True)
    Languages = models.CharField(max_length=100)
    Periodicity = models.CharField(max_length=100,choices=PERIODICITY_CHOICES,default='Daily')
    Uploading_By = models.CharField(max_length=100,choices=UPLOADING_CHOICES,default='Single_File')
    user = models.ForeignKey(User,null=True,on_delete=models.CASCADE, related_name='user')
    Type = models.CharField(max_length=100,choices=TYPE_CHOICES,default='National')

    def __str__(self):
        return str(self.Publishing_Name)

class NewsPap(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(null=True)
    image = models.ImageField(blank=True,null=True)

    def __str__(self):
        return str(self.name)

class Magazines(models.Model):
    Publishing_House = models.CharField(max_length=100)
    Magazine_Name = models.CharField(max_length=100)
    Add_Thumbnail = models.FileField(upload_to='Magazine_Thumbnails/')
    Add_Magazine = models.FileField(upload_to='Magazines/')
    Language = models.CharField(max_length=100)
    Category = models.CharField(max_length=100,choices=CATEGORY_CHOICES)
    user = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    Periodicity = models.CharField(max_length=100,choices=PERIODICITY_CHOICES)
    State = models.CharField(max_length=400)
    Uploaded_at = models.CharField(max_length=100)

    def __str__(self):
        return str(self.Magazine_Name)