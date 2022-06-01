from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from video_hosting.models import User, Channel
from video_hosting.serializers import UserCreateCustomSerializer, UserSubscriptionsSerializer, ChannelSerializer, \
    UserSubsciber


class ListUsersView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateCustomSerializer


@permission_classes((IsAuthenticated,))
class ChannelSubscribeView(APIView):

    def post(self, request):
        channel_id = request.data.get('channel_id')
        channel = Channel.objects.get(id=channel_id)
        subscriber = User.objects.get(id=request.user.id)
        subscriber.subscriptions.add(channel)
        subscriber.save()
        serialized = UserSubscriptionsSerializer(subscriber).data
        return Response(serialized)

    def delete(self, request, pk):
        # channel_id = Channel.objects.get(id=pk)
        channel = Channel.objects.get(id=pk)
        user_id = request.user.id
        channel.subscribers.remove(User.objects.get(id=user_id))
        return Response(status=status.HTTP_204_NO_CONTENT)


    def get(self, request, pk):
        channel = Channel.objects.get(id=pk)
        serialized = ChannelSerializer(channel).data
        return Response(serialized)

class UserSubscriptionsView(APIView):
    # def get(self, request, pk):
    #     user = User.objects.get(id=pk)
    #     serialized = UserSubsciber(user).data
    #     return Response(serialized)
    def get(self,request,pk):
        user=User.objects.get(id=pk)
        channel_id=request.data.get("channel_id")
        user.subscriptions.filter(Channel.objects.filter(id=channel_id))




class ResetPasswordView(APIView):
    def post(self, request):
        user_id = request.user.id
        password = request.data.get('password')
        user = User.objects.get(id=user_id)
        user.set_password(password)
        user.save()
        return Response({"message": "password changed successfull"})
