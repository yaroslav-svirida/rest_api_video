from django.shortcuts import render
from rest_framework import generics

from video_hosting.models import *
from video_hosting.serializers import VideoSerializers, CommentSerializers


class VideoAPIList(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializers


class VideoAPIListSingle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializers

# class VideoAPIListSingle(generics.RetrieveAPIView):
#     queryset = Video.objects.all()
#     serializer_class = VideoSerializers
#
# class CommentAPIList(generics.ListCreateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializers
#
#
# class CommentAPIListSingle(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializers