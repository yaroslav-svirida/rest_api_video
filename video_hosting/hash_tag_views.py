from rest_framework import generics

from video_hosting.models import HashTag
from video_hosting.serializers import HashTegSerializer


class HashTagListCreateView(generics.ListCreateAPIView):
    serializer_class = HashTegSerializer
    queryset = HashTag.objects.all()


class HashTagListRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HashTegSerializer
    queryset = HashTag.objects.all()



