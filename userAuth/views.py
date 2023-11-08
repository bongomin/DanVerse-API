from django.shortcuts import render
from .serializer import UserSerializer
from .models import CustomUser
from rest_framework import viewsets



class UserViewset(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
