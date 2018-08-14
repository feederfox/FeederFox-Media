from rest_framework import serializers
from .models import Ebook,Magazine,SocialChannel,NationalNewsChannel,RegionalNewsChannel,NationalNewsPaper,RegionalNewsPaper

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

class NewsChannelsSerializer(serializers.Serializer):
    NationalNewsChannels = NationalNewsChannelSerializer()
    RegionalNewsChannels = RegionalNewsChannelSerializer()

class ContentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Ebook,Magazine,SocialChannel
		fields = '__all__'