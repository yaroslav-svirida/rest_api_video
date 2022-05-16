from django.db import models
from django.contrib.auth.models import User, AbstractUser


# Create your models here.


class Channels(models.Model):
    name=models.CharField(max_length=255)
    description = models.TextField()
    user=models.ManyToManyField('User')



class User(AbstractUser):
    subscriptions=models.ManyToManyField(Channels)


class Video(models.Model):
    name = models.CharField(max_length=255, default='Untitled')
    title = models.CharField(max_length=255, default='Empty')
    uploaded = models.DateTimeField(auto_now_add=True, blank=True)
    likes_count = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    link = models.URLField(max_length=255, null=False, blank=False)

    def __str__(self):
        return f'{self.name}-{self.id}'


class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, blank=False, null=False, related_name='comments')
    content = models.TextField()
    likes_count = models.IntegerField(default=0)


class HashTag(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, blank=True, null=True)
    tag = models.CharField(max_length=255, default='#')


class VideoRecomendation(models.Model):
    videos = models.ManyToManyField(Video, blank=True, null=True, related_name='recommendation')
    recommendation_name = models.CharField(max_length=255, default='')
    is_top_rated = models.BooleanField()





