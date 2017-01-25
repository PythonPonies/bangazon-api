from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from bangazonapi.serializers import UserSerializer
from bangazonapi.models import User
from rest_framework import generics

#user viewset makes sense of the request and produces the appropriate output
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
