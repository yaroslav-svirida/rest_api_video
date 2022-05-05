from django.urls import path

from video_hosting.hash_tag_views import HashTagListRetrieveUpdateDeleteView, HashTagListCreateView
from video_hosting.serializers import HashTegSerializer
from video_hosting.video_views import *
from video_hosting.comment_view import *

urlpatterns = [
    path('v1/video/', VideoAPIList.as_view()),
    path('v1/video/<int:pk>', VideoAPIListSingle.as_view()),



    path('v1/comment/', CommentAPIList.as_view()),
    path('v1/comment/<int:pk>', CommentAPIListSingle.as_view()),
]

urlpatterns +=[
    path('comment/create/', CommentView.as_view()),
    path('comment/get/<int:pk>', CommentView.as_view()),
    path('comment/get/', CommentView.as_view())
]

urlpatterns+=[
    path('hashtag/', HashTagListCreateView.as_view()),
    path('hashtag/<int:pk>',HashTagListRetrieveUpdateDeleteView.as_view())
]