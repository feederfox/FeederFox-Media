from rest_framework import serializers,exceptions
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
from .models import NewsFeed


class NewsFeedSerializer(serializers.ModelSerializer):
	class Meta:
		model = NewsFeed
		fields = '__all__'
		depth = 1