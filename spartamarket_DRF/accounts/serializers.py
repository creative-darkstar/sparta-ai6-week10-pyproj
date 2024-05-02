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

    def create(self, validated_data):
        # validated_data 에서 password 분리
        password = validated_data.pop('password', None)
        # UserInfo 인스턴스 생성
        # UserInfo는 AbstractUser를 상속받은 클래스
        # AbstractUser는 AbstractBaseUser를 상속받은 클래스
        instance = self.Meta.model(**validated_data)
        if password is not None:
            # AbstractBaseUser 의 method를 사용해 암호화
            # UserInfo는 AbstractBaseUser 의 method를 사용할 수 있음
            instance.set_password(password)

        instance.first_name = validated_data.get("first_name").lower()
        instance.last_name = validated_data.get("last_name").lower()

        instance.save()
        return instance
