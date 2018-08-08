from django.db import models
from django.contrib.auth.models import User
# Create your models here.

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


# class Uploader_Contact_Details(models.Model):
#     Name = models.CharField(max_length=100)
#     Mobile = models.PositiveIntegerField()
#     LandLine = models.PositiveIntegerField()
#     Email = models.EmailField()

#     def __str__(self):
#         return str(self.Name)

# class Posts(models.Model):
#     Publishing_House = models.CharField(max_length=100)
#     Publishing_Name = models.CharField(max_length=100)
#     Add_Logo = models.FileField(upload_to='media/')
#     Number_of_Editions = models.PositiveIntegerField()
#     Sub_Editions = models.CharField(max_length=100)
#     Place = models.CharField(max_length=400)
#     Languages = models.CharField(max_length=100)
#     Periodicity = models.CharField(max_length=100,choices=PERIODICITY_CHOICES,default='Daily')
#     Uploading_By = models.CharField(max_length=100,choices=UPLOADING_CHOICES,default='Single_File')
#     Uploader_Contact_Details = models.ForeignKey(User,on_delete=models.CASCADE)

#     def __str__(self):
#         return str(self.Publishing_Name)


    # post = models.CharField(max_length=500)
    # name = models.CharField(max_length=140, default='SOME STRING')
    # language = models.CharField(max_length=140, default='SOME STRING')
    # email = models.EmailField(max_length=140, default='SOME STRING')
    # # picture = models.ImageField(upload_to='img')
    # sample_chapter = models.FileField(blank=True, null=True,
    #                                    upload_to="chapters/%Y/%m/$D/")
    # cover_image = models.ImageField(blank=True, null=True,
    #                                 upload_to="covers/%Y/%m/%D/")
    # favorite_fruit = models.CharField( max_length=500, null=True,)
    # state = models.CharField(max_length=500, null=True, )
    # user = models.ForeignKey(User,on_delete=models.CASCADE,)

