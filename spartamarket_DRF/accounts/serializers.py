from rest_framework import serializers
from .models import UserInfo


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = "__all__"
        read_only_fields = (

        )

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret.pop("password")
        ret.pop("last_login")
        ret.pop("is_superuser")
        ret.pop("is_staff")
        ret.pop("is_active")
        ret.pop("groups")
        ret.pop("user_permissions")
        return ret

    # def save(self):
    #     email = self.validated_data['email'].lower()
    #     username = self.validated_data['username'].lower()
    #     first_name = self.validated_data['first_name'].lower()
    #     last_name = self.validated_data['last_name'].lower()
