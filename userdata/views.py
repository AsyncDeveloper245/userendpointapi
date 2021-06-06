from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView,ListAPIView
from .serializers import CustomUserSerializer
from django.contrib.auth import get_user_model


# Create your views here.
class CustomUserListAPIView(ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = CustomUserSerializer


class CustomUserDetailAPIView(RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = CustomUserSerializer
