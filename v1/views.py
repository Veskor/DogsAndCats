from django.shortcuts import render
from .serializers import *
from rest_framework import permissions
from .permissions import *
# Create your views here.

class DogViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    serializer_class = DogSerializer
    queryset = serializer_class.Meta.model.objects.all()

    def __str__(self):
        return self.name

class CatViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    serializer_class = CatSerializer
    queryset = serializer_class.Meta.model.objects.all()

    def __str__(self):
        return self.name
