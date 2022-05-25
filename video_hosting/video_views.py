from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from video_hosting.models import *
from video_hosting.serializers import VideoSerializers, CommentSerializers, VideoFullSerializers


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
        video_data = request.data
        user_id = request.data.get("user_id")
        user = User.objects.get(id =user_id)
        video = Video.objects.create(user=user,**video_data)
        serialized_video = VideoSerializers(video).data
        return Response(serialized_video)

    @method_decorator(cache_page(60*2))
    @method_decorator(vary_on_cookie)
    def get(self, request, pk=None):
        try:
            if not pk:
                videos = Video.objects.all()
                video_serialized = VideoSerializers(videos, many=True).data
                return Response(video_serialized)

            video = Video.objects.filter(id=pk, user=user)
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
            video = Video.objects.get(pk=pk)

        except Video.DoesNotExist:
            raise Http404
        video.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OnlyMyVideoView(APIView):
    def get(self, request):
        user = request.user
        videos = Video.objects.filter(user=user)
        serializer_video = VideoFullSerializers(videos).data
        return Response(serializer_video)
