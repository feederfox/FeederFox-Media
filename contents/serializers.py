from rest_framework import serializers
from .models import Ebook,Magazine,SocialChannel,NationalNewsChannel,RegionalNewsChannel,NationalNewsPaper,RegionalNewsPaper,Article
from accounts.models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


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


class RegionalNewsChannelSerializer(serializers.ModelSerializer):
	class Meta:
		model = RegionalNewsChannel
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

class SignupSerializer(serializers.ModelSerializer):

	Application_type = serializers.ChoiceField(choices=ACCCOUNT_CHOICES)


	class Meta:
		model = User
		fields = ('username','email','password','Application_type')
		extra_kwargs = {"password":{"write_only":True}}

	def create(self, validated_data, *args, **kwargs):
		# username = request.POST.get('username')
		# email = request.POST.get('email')
		# password = request.POST.get('password')
		# Application_type = request.POST.get('Application_type')
		# user = User.objects.create_user(username,email,password)
		# user.Application_type = Application_type
		# user.save()

		email = validated_data['email']
		username = validated_data['username']
		password = (validated_data['password'])
		Application_type = validated_data['Application_type']
		user = User(
				username = username,
				email = email,
				password = password
			)   
		user.set_password(password)
		
		user.save()
		user.Application_type = Application_type
		user.Account_type = 2
		#user.profile = Profile.objects.create(user=user.profile.user)
		user.profile.username = user.username
		user.profile.email = user.email
		user.profile.Application_type = user.Application_type
		user.profile.Account_type = user.Account_type

		user.profile.save()

		print(user)
		print(user.profile.user)
		print(user.profile.Account_type)
		print(user.profile.Application_type)
		print(user.profile.username)
		print(user.password)
		print(user.profile.email)
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
		fields = ('username','password')

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