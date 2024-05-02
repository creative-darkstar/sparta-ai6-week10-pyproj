from rest_framework import serializers
from .models import ProductInfo


class ProductSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = ProductInfo
        fields = "__all__"
        read_only_fields = (
            "user",
        )

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret.pop("is_visible")
        ret.pop("user")
        return ret


class ProductListSerializer(ProductSerializer):
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret.pop("content")
        return ret
