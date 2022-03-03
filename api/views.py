from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from api.models import SomeModel
from api.serializer import SomeModelSerializer


# from rest_framework.response import Response

class SomeModelCreateApi(generics.CreateAPIView):
    """ Create some-model instance """
    queryset = SomeModel.objects.all()
    serializer_class = SomeModelSerializer


class SomeModelListApi(generics.ListAPIView):
    """ Show all some-model instances """
    queryset = SomeModel.objects.all()
    serializer_class = SomeModelSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['name', 'amount', 'distance']
    search_fields = ['name']


class SomeModelUpdateApi(generics.RetrieveUpdateAPIView):
    """ Update a some-model instance's part by pk """
    queryset = SomeModel.objects.all()
    serializer_class = SomeModelSerializer


class SomeModelDeleteApi(generics.DestroyAPIView):
    """ Update a some-model instance's part by pk """
    queryset = SomeModel.objects.all()
    serializer_class = SomeModelSerializer