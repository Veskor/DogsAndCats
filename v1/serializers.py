from .models import *
from rest_framework import serializers,viewsets
from django.contrib.auth.models import User

class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = ('id','name','birthday','owner')

class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = ('id','name','birthday','owner')
