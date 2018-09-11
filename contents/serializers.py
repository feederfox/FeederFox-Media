from rest_framework import serializers,exceptions
from .models import Ebook,Magazine,SocialChannel,NationalNewsChannel,RegionalNewsChannel,NationalNewsPaper,RegionalNewsPaper,Article,NewsPaper
from accounts.models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from rest_framework import status
from django.dispatch import receiver
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError


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

class SignupSerializer(serializers.ModelSerializer):
	username = serializers.CharField()
	Application_type = serializers.ChoiceField(choices=ACCCOUNT_CHOICES)


	class Meta:
		model = User
		fields = ('username','email','password','Application_type')
		extra_kwargs = {"password":{"write_only":True}}

	# def create(self, request, *args, **kwargs):
	# 	serializer = self.get_serializer(data=request.data)
 #        serializer.is_valid(raise_exception=True)
 #        self.perform_create(serializer)

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
		#headers = self.get_success_headers(validated_data)
		#return validated_data

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