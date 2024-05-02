from django.shortcuts import get_list_or_404, get_object_or_404

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import UserInfo
from .serializers import (
    UserSerializer
)


class UserAPIView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserProfileAPIView(APIView):
    # APIView permission_classes override
    # Check user's auth. If it is valid, proceed class funcs.
    permission_classes = [IsAuthenticated]

    def get(self, request, username):
        username = username.lower()
        user = get_object_or_404(UserInfo, username=username)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
