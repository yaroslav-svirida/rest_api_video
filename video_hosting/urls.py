from django.urls import path

from video_hosting.hash_tag_views import HashTagListRetrieveUpdateDeleteView, HashTagListCreateView
from video_hosting.serializers import HashTegSerializer
from video_hosting.users_views import ListUsersView, ResetPasswordView, ChannelSubscribeView, UserSubscriptionsView
from video_hosting.video_views import *
from video_hosting.comment_view import *

urlpatterns = [
    path('video/create/', VideoView.as_view()),
    path('video/get/<int:pk>', VideoView.as_view()),
    path('video/get/', VideoView.as_view()),
    path('video/get-my/', OnlyMyVideoView.as_view()),
    path('video/update/<int:pk>', VideoView.as_view()),
    path('video/delete/<int:pk>', VideoView.as_view()),


    #
    # path('v1/comment/', CommentAPIList.as_view()),
    # path('v1/comment/<int:pk>', CommentAPIListSingle.as_view()),
]

urlpatterns +=[
    path('comment/create/', CommentView.as_view()),
    path('comment/get/<int:pk>', CommentView.as_view()),
    path('comment/get/', CommentView.as_view()),
    path('comment/update/<int:pk>', CommentView.as_view()),
    path('comment/delete/<int:pk>', CommentView.as_view()),

]

urlpatterns += [
    path('hashtag/', HashTagListCreateView.as_view()),
    path('hashtag/<int:pk>',HashTagListRetrieveUpdateDeleteView.as_view())
]
urlpatterns += [
    path('password/rest_password/', ResetPasswordView.as_view())
]
#
# urlpatterns+=[
#     path('users/', ListUsersView.as_view())
# ]
urlpatterns+=[
    path("subscribe/", ChannelSubscribeView.as_view()),
    path("subscribe/get_all/<int:pk>", ChannelSubscribeView.as_view()),
    path("subscribe/delete/<int:pk>", ChannelSubscribeView.as_view()),

    ]
#
# urlpatterns+=[
#     path("subscribe/get_user/<int:pk>", UserSubscriptionsView.as_view()),
#
#
#     ]