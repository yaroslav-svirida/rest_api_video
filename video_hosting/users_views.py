from rest_framework.generics import ListAPIView

from video_hosting.models import User
from video_hosting.serializers import UserCreateCustomSerializer


class ListUsersView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateCustomSerializer