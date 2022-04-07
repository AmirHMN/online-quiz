from djoser.serializers import UserSerializer as BaseUserSerializer, UserCreateSerializer as BaseUserCreateSerializer
from .models import User


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'national_code', 'password']


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['first_name', 'last_name']
