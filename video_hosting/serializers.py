from rest_framework import serializers
from .models import *

class VideoSerializers(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'likes_count', 'user')
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