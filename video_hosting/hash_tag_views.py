from rest_framework import generics

from video_hosting.models import HashTag
from video_hosting.pagination import HashTagPagination
from video_hosting.serializers import HashTegSerializer


class HashTagListCreateView(generics.ListCreateAPIView):
    serializer_class = HashTegSerializer
    queryset = HashTag.objects.all()
    pagination_class = HashTagPagination


class HashTagListRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HashTegSerializer
    queryset = HashTag.objects.all()

    # def get_queryset(self):
    #     id = self.kwars['id']
    #     hast_tags = HashTag.objects.filter(id=id)
    #     return hast_tags



