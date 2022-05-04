from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView

from video_hosting.models import *
from video_hosting.serializers import VideoSerializers, CommentSerializers



class CommentAPIList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers


class CommentAPIListSingle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers


class CommentView(APIView):

    def post(self, request):
        video_id=request.data.get('video')
        content=request.data.get('content')
        video=Video.objects.get(id=video_id)

        comment = Comment.objects.create(video=video, content=content)
        comment_serialized= CommentSerializers(comment).data
