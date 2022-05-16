from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from video_hosting.models import *
from video_hosting.serializers import VideoSerializers, CommentSerializers


#
# class CommentAPIList(generics.ListCreateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializers
#
#
# class CommentAPIListSingle(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializers


class CommentView(APIView):

    def post(self, request):
        video_id=request.data.get('video')
        content=request.data.get('content')
        video=Video.objects.get(id=video_id)

        comment = Comment.objects.create(video=video, content=content)
        comment_serialized= CommentSerializers(comment).data
        return Response(comment_serialized)

    def get(self, request, pk=None):
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

    # def put(self, request,pk):
    #     comment = Comment.objects.get(id=pk)
    #     content=request.data.get('content')
    #
    #
    #     comment = Comment.objects.update(comment=comment, content=content)
    #     comment_serialized= CommentSerializers(comment).data
    #     return Response(comment_serialized)

    def put(self, request, pk):
        com = Comment.objects.get(id=pk)
        serializer = CommentSerializers(com, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





    # def put(self, request, *args, **kwargs):
    #     pk = kwargs.get("pk", None)
    #     if not pk:
    #         return Response({"error": "Method PUT not allowed"})
    #
    #     try:
    #         instance = Comment.objects.get(pk=pk)
    #     except:
    #         return Response({"error": "Object does not exists"})
    #
    #     serializer = CommentSerializers(data=request.data, instance=instance)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #
    #     return Response({"post": serializer.data})

    def delete(self, request, pk):
        try:
            com=Comment.objects.get(pk=pk)

        except Comment.DoesNotExist:
            raise Http404
        com.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

