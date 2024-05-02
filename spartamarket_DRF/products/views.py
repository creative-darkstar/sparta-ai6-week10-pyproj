from django.shortcuts import render, get_list_or_404, get_object_or_404

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ProductInfo
from .serializers import (
    ProductSerializer,
    ProductListSerializer,
)


class ProductListAPIView(APIView):
    # APIView permission_classes override
    # Check user's auth. If it is valid, proceed class funcs.
    permission_classes = [IsAuthenticated]

    def get(self, request):
        rows = ProductInfo.objects.filter(is_visible=True)
        serializer = ProductListSerializer(rows, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(
                user=request.user
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProductDetailAPIView(APIView):
    # APIView permission_classes override
    # Check user's auth. If it is valid, proceed class funcs.
    permission_classes = [IsAuthenticated]

    def get(self, request, productId):
        row = get_object_or_404(ProductInfo, pk=productId, is_visible=True)
        serializer = ProductSerializer(row)
        return Response(serializer.data)

    def put(self, request, productId):
        row = get_object_or_404(ProductInfo, pk=productId, is_visible=True)
        if request.user.id != row.user.id:
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = ProductSerializer(data=request.data, instance=row, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request, productId):
        row = get_object_or_404(ProductInfo, pk=productId, is_visible=True)
        if request.user.id != row.user.id:
            return Response(status=status.HTTP_403_FORBIDDEN)

        row.is_visible = False
        row.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
