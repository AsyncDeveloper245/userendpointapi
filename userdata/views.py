from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView,ListAPIView
from .serializers import CustomUserSerializer
from django.contrib.auth import get_user_model
from rest_framework_api_key.permissions import HasAPIKey


# Create your views here.
class CustomUserListAPIView(ListAPIView):
    permission_classes = (HasAPIKey,)
    queryset = get_user_model().objects.all()
    serializer_class = CustomUserSerializer


class CustomUserDetailAPIView(RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = CustomUserSerializer

