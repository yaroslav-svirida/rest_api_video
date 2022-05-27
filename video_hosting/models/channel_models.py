from django.db import models


from video_hosting.models import User


class Channel(models.Model):
    name = models.CharField(max_length=255, default="Untitled")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='channel')
