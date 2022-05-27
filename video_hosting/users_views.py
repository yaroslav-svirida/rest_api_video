
from rest_framework.decorators import permission_classes
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from video_hosting.models import User, Channel
from video_hosting.serializers import UserCreateCustomSerializer, UserSubscriptionsSerializer, ChannelSerializer


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

    def get(self, request, pk):
        channel = Channel.objects.get(id=pk)
        serialized = ChannelSerializer(channel).data
        return Response(serialized)


class ResetPasswordView(APIView):
    def post(self, request):
        user_id = request.user.id
        password = request.data.get('password')
        user = User.objects.get(id=user_id)
        user.set_password(password)
        user.save()
        return Response({"message": "password changed successfull"})
