from rest_framework import serializers
from .models import Ebook,Magazine,SocialChannel,NationalNewsChannel,RegionalNewsChannel,NationalNewsPaper,RegionalNewsPaper,Article
from accounts.models import Profile
from django.contrib.auth.models import User

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
	password1 = serializers.CharField()
	password2 = serializers.CharField()
	Application_Type = serializers.ChoiceField(choices=ACCCOUNT_CHOICES)


	class Meta:
		model = User
		fields = ('username','email','password1','password2','Application_Type')

	def create(self, validated_data):
		user = super(SignupSerializer, self).create(validated_data)
		user.set_password(validated_data['password1'])
		user.save
		return User.objects.create(**user)
	# def create(self, validated_data):
	# 	user = super(SignupSerializer, self).create(validated_data)
	# 	user.set_password(validated_data['password1'])
	# 	user.save()
	# 	return user

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    Application_Type = serializers.ChoiceField(choices=ACCCOUNT_CHOICES)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'Application_Type')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
