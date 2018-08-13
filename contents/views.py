from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Ebook,Magazine,SocialChannel
from .serializers import EbookSerializer,MagazineSerializer,SocialChannelSerializer


@api_view(['GET', 'POST'])
def ebook_list(request):
    if request.method == 'GET':
        ebook = Ebook.objects.all()
        serializer = EbookSerializer(ebook, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = EbookSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def magazine_list(request):
    if request.method == 'GET':
        magazine = Magazine.objects.all()
        serializer = MagazineSerializer(magazine_list, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MagazineSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def socialchannels_list(request):
    if request.method == 'GET':
        socialchannel = SocialChannel.objects.all()
        serializer = SocialChannelSerializer(socialchannel, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SocialChannelSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

