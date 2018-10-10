from rest_framework import serializers
from .models import Newsfeeds

class NewsfeedsSerializers(serializers.ModelSerializer):
	class Meta:
		model= Newsfeeds
		fields = '__all__'

# class HeadlinesSerializers(serializers.ModelSerializer):
# 	class Meta:
# 		model= Newsfeeds
# 		fields = '__all__'