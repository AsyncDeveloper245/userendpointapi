from django.urls import path,include
from . import views



urlpatterns = [
    path('',views.CustomUserListAPIView().as_view(),name = 'users_list'),
    path('<int:pk>',views.CustomUserDetailAPIView.as_view(),name = 'users_detail'),

]