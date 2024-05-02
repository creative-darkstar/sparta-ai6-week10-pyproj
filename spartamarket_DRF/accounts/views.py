from django.shortcuts import get_list_or_404, get_object_or_404

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

import re

from .models import UserInfo
from .serializers import (
    UserSerializer
)


class UserAPIView(APIView):

    # 정규표현식 패턴 상수
    USERNAME_PATTERN = re.compile(r'^[a-zA-Z0-9_]{4,20}$')
    EMAIL_PATTERN = re.compile(r'^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    NICKNAME_PATTERN = re.compile(r'^[a-zA-Z0-9_]{4,20}$')

    def post(self, request):
        check = {
            "username": request.data.get("username", None),
            "email": request.data.get("email", None),
            "nickname": request.data.get("nickname", None),
        }
        if check["username"] is None or check["email"] is None or check["nickname"] is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        # username validation
        username = check["username"].lower()
        if not self.USERNAME_PATTERN.match(username):
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        request.data["username"] = username

        # email validation
        email = check["email"].lower()
        if not self.EMAIL_PATTERN.match(email):
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        request.data["email"] = email

        # nickname validation
        nickname = check["nickname"].lower()
        if not self.NICKNAME_PATTERN.match(nickname):
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        request.data["nickname"] = nickname

        # 모든 유효성 통과 후 serialize
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
