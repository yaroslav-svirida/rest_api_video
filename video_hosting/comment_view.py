from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
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
        return Response(comment_serialized)

    def get(self, pk=None):
        try:
            if not pk:
                comments = Comment.objects.all()
                comment_serialized = CommentSerializers(comments, many=True).data
                return Response(comment_serialized)
            comment = Comment.objects.get(id=pk)
            comment_serialized = CommentSerializers(comment).data
            return Response(comment_serialized)
        except ObjectDoesNotExist as e:
            return Response(status=status.HTTP_404_NOT_FOUND)

