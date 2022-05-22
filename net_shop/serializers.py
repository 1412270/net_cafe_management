from rest_framework.serializers import ModelSerializer
from .models import *


class UserSerializer(ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email", "phone", "wallet"]
        extract_kwargs = {
            'password': {'write_only': 'true'}
        }
