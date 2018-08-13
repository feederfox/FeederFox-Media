from rest_framework import serializers
from .models import Ebook,Magazine,SocialChannel

class EbookSerializer(serializers.ModelSerializer):
	class Meta:
		model = Ebook
		fields = ('ebooks_name','ebooks_url','ebooks_image')

class MagazineSerializer(serializers.ModelSerializer):
	class Meta:
		model = Magazine
		fields = ('magazine_name','magazine_url','magazine_image')

class SocialChannelSerializer(serializers.ModelSerializer):
	class Meta:
		model = SocialChannel
		fields = ('socialchannels_name','socialchannels_url','socialchannels_image')