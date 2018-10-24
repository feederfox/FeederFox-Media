from rest_framework import serializers,exceptions
from .models import (Ebook,Magazine,SocialChannel,NationalNewsChannel,RegionalNewsChannel,NationalNewsPaper,RegionalNewsPaper,
			Article,NewsPaper,Dummy,PublisherDetail,Edition,NewsChannel,PoliticalForum,PoliticalPosition,EbookUpload,
			Article_upload,Polling,PoliticianArticle,Vote,PoliticalSurvey,State,PoliticalCommentSystem)
from accounts.models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from rest_framework import status
from django.dispatch import receiver
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import HyperlinkedIdentityField
from django.contrib.auth.forms import PasswordResetForm
from django.conf import settings
from django.utils.translation import gettext as _




class UserException(exceptions.ValidationError):
	status_code = status.HTTP_200_OK

class EmailException(exceptions.ValidationError):
	status_code = status.HTTP_200_OK

class EbookSerializer(serializers.ModelSerializer):
	class Meta:
		model = Ebook
		fields = '__all__'

class MagazineSerializer(serializers.ModelSerializer):
	class Meta:
		model = Magazine
		fields = '__all__'

class SocialChannelSerializer(serializers.ModelSerializer):
	class Meta:
		model = SocialChannel
		fields = '__all__'

class NationalNewsChannelSerializer(serializers.ModelSerializer):
	class Meta:
		model = NationalNewsChannel
		fields = '__all__'

class DummySerializer(serializers.ModelSerializer):
	class Meta:
		model = Dummy
		fields = '__all__'

class NewsChannelSerializer(serializers.ModelSerializer):
	class Meta:
		model = NewsChannel
		fields = '__all__'

class RegionalNewsChannelSerializer(serializers.ModelSerializer):
	class Meta:
		model = RegionalNewsChannel
		fields = '__all__'

class NewsPaperSerializer(serializers.ModelSerializer):
	class Meta:
		model = NewsPaper
		fields = '__all__'

class NationalNewsPaperSerializer(serializers.ModelSerializer):
	class Meta:
		model = NationalNewsPaper
		fields = '__all__'

class RegionalNewsPaperSerializer(serializers.ModelSerializer):
	class Meta:
		model = RegionalNewsPaper
		fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Article
		fields = '__all__'

		

ACCCOUNT_CHOICES = [
    ('1','Android'),
    ('2','IOS'),
]

LOGIN_CHOICES = [
	('0','Normal'),
	('1','Facebook'),
	('2','GooglePlus'),
]



class SignupSerializer(serializers.ModelSerializer):
	username = serializers.CharField()
	Application_type = serializers.ChoiceField(choices=ACCCOUNT_CHOICES)


	class Meta:
		model = User
		fields = ('username','email','password','Application_type')
		extra_kwargs = {"password":{"write_only":True}}


	def create(self, validated_data, *args, **kwargs):
		email = validated_data['email']
		username = validated_data['username']
		password = (validated_data['password'])
		Application_type = validated_data['Application_type']
		u = User.objects.filter(username=username)
		if u:
			raise UserException({'detail':'Username is already in use'})
		e = User.objects.filter(email=email)
		if e:
		    raise EmailException({'detail':'Email already in use'})
		user = User(
				username = username,
				email = email,
				password = password
			)
		user.set_password(password)
		user.save()
		user.Application_type = Application_type
		user.Account_type = 2
		user.profile.username = user.username
		user.profile.email = user.email
		user.profile.Application_type = user.Application_type
		user.profile.Account_type = user.Account_type
		user.profile.save()

		if user:
			return validated_data

class SignupAPISerializer(serializers.ModelSerializer):
	username = serializers.CharField()
	Application_type = serializers.ChoiceField(choices=ACCCOUNT_CHOICES)
	Profile_Picture = serializers.ImageField(write_only=True)
	Mobile = serializers.IntegerField()
	
	class Meta:
		model = User
		fields = ('username','email','password','Profile_Picture','Mobile','Application_type',
			)
		extra_kwargs = {"password":{"write_only":True},"Profile_Picture":{"write_only":True}}


	def create(self, validated_data, *args, **kwargs):
		email = validated_data['email']
		username = validated_data['username']
		password = (validated_data['password'])
		Application_type = validated_data['Application_type']
		Profile_Picture = validated_data['Profile_Picture']
		Mobile = validated_data['Mobile']
		u = User.objects.filter(username=username)
		if u:
			raise UserException({'status_code':0,'detail':'Username is already in use'})
		e = User.objects.filter(email=email)
		if e:
		    raise EmailException({'status_code':0,
                'detail':'Email already in use'})
		user = User(
				username = username,
				email = email,
				password = password
			)
		user.set_password(password)
		user.save()
		user.Application_type = Application_type
		user.Account_type = 2
		user.Profile_Picture = Profile_Picture
		user.Mobile = Mobile
		user.Social_login = 0
		user.profile.username = user.username
		user.profile.email = user.email
		user.profile.Application_type = user.Application_type
		user.profile.Account_type = user.Account_type
		user.profile.Profile_Picture = user.Profile_Picture
		user.profile.Mobile = user.Mobile
		user.profile.Social_login = 0
		user.profile.save()

		if user:
			return validated_data

	# @receiver(post_save, sender=User)
	# def update_user_profile(sender, instance, created, **kwargs):
	# 	if created:
	# 		Profile.objects.create(user=instance)
	# 	instance.profile.save()

	# def create(self, validated_data):
	# 	user = super(SignupSerializer, self).create(validated_data)
	# 	user.set_password(validated_data['password1'])
	# 	user.save
	# 	return User.objects.create(**user)
	# def create(self, validated_data):
	# 	user = super(SignupSerializer, self).create(validated_data)
	# 	user.set_password(validated_data['password1'])
	# 	user.save()
	# 	return user

class LoginSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('email','password')

	def validate(self, data):
		return data

# class UserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)
#     Application_Type = serializers.ChoiceField(choices=ACCCOUNT_CHOICES)

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password', 'Application_Type')

#     def create(self, validated_data):
#         user = super(UserSerializer, self).create(validated_data)
#         user.set_password(validated_data['password'])
#         user.save()
#         return user

# class UserCreateSerializer(serializers.ModelSerializer):
# 	Application_Type = serializers.ChoiceField(choices=ACCCOUNT_CHOICES)

# 	@staticmethod
# 	def validate(self, data, *args, **kwargs):
# 		email = data['email']
# 		user_qs = User.objects.filter(email=email)
# 		if user_qs:
# 			raise validationError("This User is Already Registered")
# 		return data

# 	@staticmethod
# 	def create(self, validated_data, *args, **kwargs):
# 		email = validated_data['email']
# 		username = validated_data['username']
# 		password = validated_data['password']
# 		Application_Type = validated_data['Application_Type']
# 		user_obj = User(
# 				username = username,
# 				email = email,
# 			)
# 		user_obj.set_password(password)
# 		user_obj.save()
# 		return validated_data

# 	class Meta:
# 		model = UserSerializer
# 		fields = ('username','email','password','Application_Type')
# 		extra_kwargs = {"password":{"write_only":True}}
#

class EditionSerializer(serializers.ModelSerializer):
	#url = serializers.URLField()
	class Meta:
		model = Edition
		fields = ('Name',)

class PublisherListSerializer(serializers.ModelSerializer):
	Sub_Edition = EditionSerializer(read_only=True, many=True)
	#url = HyperlinkedIdentityField(view_name='content:pub')

	class Meta:
		model = PublisherDetail
		fields = ('id','Name','Language','Add_Logo','State','Main_Edition','Sub_Edition')
		depth = 1

class StateSerializer(serializers.ModelSerializer):
	class Meta:
		model = State
		fields = ('name',)

class PublisherDetailSerializer(serializers.ModelSerializer):
	State = StateSerializer(read_only=True)
	class Meta:
		model = PublisherDetail
		fields = ('id','Name','Language','Add_Logo','State','Sub_Edition')
		depth = 2

class PoliticalPositionSerializer(serializers.ModelSerializer):
	class Meta:
		model = PoliticalPosition
		exclude = ('id',)


class PoliticalForumSerializer(serializers.ModelSerializer):
	url = HyperlinkedIdentityField(view_name='content:politicalforumapi')
	class Meta:
		model = PoliticalForum
		fields = '__all__'
		depth = 1

class PoliticalForumAPISerializer(serializers.ModelSerializer):
	class Meta:
		model = PoliticalForum
		fields = '__all__'
		depth = 1		

class PollingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Polling
		fields = '__all__'
		depth = 1

class PoliticianArticleSerializer(serializers.ModelSerializer):
	class Meta:
		model = PoliticianArticle
		fields = '__all__'
		depth = 1

class PoliticalSurveySerializer(serializers.ModelSerializer):
	class Meta:
		model = PoliticalSurvey
		exclude = ('Upvote','DownVote')
		depth = 1		

class PoliticalVotingSerializer(serializers.Serializer):
	question_id = serializers.IntegerField()
	opinion = serializers.IntegerField()
	email = serializers.EmailField()

class PoliticalCommentSerializer(serializers.ModelSerializer):
	image = serializers.ImageField()
	class Meta:
		model = PoliticalCommentSystem
		fields = '__all__'


class EbookUpdatedSerializer(serializers.ModelSerializer):
	url = serializers.URLField(source='pdf')
	class Meta:
		model = EbookUpload
		fields = ('name','image','url','pdf','author')


class ArticleuploadSerializer(serializers.ModelSerializer):
	class Meta:
		model = Article_upload
		fields = '__all__'

class NewsPaperEditionSerializer(serializers.ModelSerializer):
	url = serializers.URLField(read_only=True)
	class Meta:
		model = NewsPaper
		fields = ('name','subedition','url')



class ForgotPasswordSerializer(serializers.Serializer):
	email = serializers.EmailField()
	password_reset_form_class = PasswordResetForm
    
	def validate_email(self, value):
		self.reset_form = self.password_reset_form_class(data=self.initial_data)
		if not self.reset_form.is_valid():
			raise serializers.ValidationError(_('Error'))

	        ###### FILTER YOUR USER MODEL ######
		if not User.objects.filter(email=value).exists():
			raise serializers.ValidationError({'detail':'PoliticalForumAPISerializer'})
		return value

	def save(self):
	    request = self.context.get('request')
	    opts = {
	        'use_https': request.is_secure(),
	        'from_email': getattr(settings, 'DEFAULT_FROM_EMAIL'),
	        'request': request,
        }
	    self.reset_form.save(**opts)
	

class profileUploadSerializer(serializers.ModelSerializer):
	url = HyperlinkedIdentityField(view_name='content:profileuploadapi')
	class Meta:
		model = Profile
		fields = ('id','url','username','email','Account_type','Firstname','Lastname','Mobile','Application_type',
			'Profile_Picture')
