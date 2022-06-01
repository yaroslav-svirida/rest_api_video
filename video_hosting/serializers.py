from rest_framework import serializers
from .models import *

from djoser.serializers import  UserCreateSerializer
from . import models

class UserCreateCustomSerializer():
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'password')



class VideoSerializers(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', "title", 'likes_count', 'link','user')
        model = Video

class VideoFullSerializers(serializers.ModelSerializer):
    class Meta:
        fields = ("__all__")
        model = Video

class CommentSerializers(serializers.ModelSerializer):
    # video=VideoSerializers(many=False)
    class Meta:
        fields = ('owner', 'video', 'content', 'likes_count')
        model = Comment

    # def update(self, instance, validated_data):
    #     instance.owner = validated_data.get('owner', instance.owner)
    #     instance.video = validated_data.get('video', instance.video)
    #     instance.content = validated_data.get('content', instance.content)
    #     instance.likes_count = validated_data.get('likes_count', instance.likes_count)
    #     instance.save()
    #     return instance


class HashTegSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model=HashTag


class VideoRecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'video', 'recommendation_name', 'is_top_rated')
        model=VideoRecomendation

class UserSubsciberChannel(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "name", "owner")
        model = Channel

class UserSubsciber(serializers.ModelSerializer):
    subscriptions =UserSubsciberChannel(many=True)
    class Meta:
        fields = ("id", "first_name", "last_name", "email","subscriptions")
        model = User


class ChannelSerializer(serializers.ModelSerializer):
    subscribers =UserSubsciber(many=True)
    class Meta:
        fields = ("id", "name", "subscribers", "owner")
        model = Channel



class UserSubscriptionsSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ("id", "email", "subscriptions")
        model = User

class ChannelsSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ("name","owner")
        model = Channel