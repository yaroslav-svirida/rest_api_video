from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from video_hosting.models import *
from video_hosting.serializers import VideoSerializers, CommentSerializers


# class VideoAPIList(generics.ListCreateAPIView):
#     queryset = Video.objects.all()
#     serializer_class = VideoSerializers
#
#
# class VideoAPIListSingle(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Video.objects.all()
#     serializer_class = VideoSerializers

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

class VideoView(APIView):

    def post(self, request):
        name=request.data.get('name')
        likes_count=request.data.get('likes_count')


        video = Video.objects.create(name=name, likes_count=likes_count)
        comment_serialized= VideoSerializers(video).data
        return Response(comment_serialized)

    def get(self, request, pk=None):
        try:
            if not pk:
                videos = Video.objects.all()
                video_serialized = VideoSerializers(videos, many=True).data
                return Response(video_serialized)
            video = Video.objects.get(id=pk)
            video_serialized = VideoSerializers(video).data
            return Response(video_serialized)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        video = Video.objects.get(id=pk)
        serializer = VideoSerializers(video, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        try:
            video=Video.objects.get(pk=pk)

        except Video.DoesNotExist:
            raise Http404
        video.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
