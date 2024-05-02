from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

app_name = "accounts"

urlpatterns = [
    path("", views.UserAPIView.as_view(), name="sign_up"),
    path("login", TokenObtainPairView.as_view(), name="login"),
    path("login/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("<str:username>", views.UserProfileAPIView.as_view(), name="user_profile"),
]