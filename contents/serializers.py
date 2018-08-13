from rest_framework import serializers
from .models import Ebook,Magazine,SocialChannel,NationalNewsChannel,RegionalNewsChannel

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

class NationalNewsChannelSerializer(serializers.ModelSerializer):
	class Meta:
		model = NationalNewsChannel
		fields = ('channel_name','channel_url','channel_image')


class RegionalNewsChannelSerializer(serializers.ModelSerializer):
	class Meta:
		model = RegionalNewsChannel
		fields = '__all__'


class NewsChannelsSerializer(serializers.Serializer):
    NationalNewsChannels = NationalNewsChannelSerializer()
    RegionalNewsChannels = RegionalNewsChannelSerializer()

class ContentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Ebook,Magazine,SocialChannel
		fields = '__all__'