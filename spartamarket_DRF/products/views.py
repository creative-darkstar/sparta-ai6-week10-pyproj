from django.shortcuts import get_list_or_404, get_object_or_404

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

    # 페이지네이션 상수
    # 한 페이지에 몇 개의 상품을 표시할지 결정
    MAX_ITEMS_PER_PAGE = 5

    def get(self, request):
        # 쿼리 스트링
        page = request.query_params.get("page", '1')
        # 쿼리 스트링이 유효하지 않은 값(숫자가 아닌 경우)일 경우 상태코드 400
        if not page.isdecimal:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        # 페이지네이션 start, end 지정
        page = int(page)
        start = (page - 1) * self.MAX_ITEMS_PER_PAGE
        end = start + self.MAX_ITEMS_PER_PAGE

        # 데이터 페이지네이션
        rows = ProductInfo.objects.filter(is_visible=True)[start:end]
        # 유요하지 않은 페이지네이션(데이터가 존재하지 않음)일 경우 상태코드 204
        # 유효하다면 serialize 진행 후 데이터 응답
        if not rows:
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
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
        # 로그인한 사용자와 상품 등록자가 다를 경우 상태코드 403
        if request.user.id != row.user.id:
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = ProductSerializer(data=request.data, instance=row, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request, productId):
        row = get_object_or_404(ProductInfo, pk=productId, is_visible=True)
        # 로그인한 사용자와 상품 등록자가 다를 경우 상태코드 403
        if request.user.id != row.user.id:
            return Response(status=status.HTTP_403_FORBIDDEN)

        # sofr delete
        # 삭제된 상품 정보 추적을 위함
        row.is_visible = False
        row.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
