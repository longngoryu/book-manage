from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "password",
            "email",
            "image_url",
            "is_staff",
            "is_active",
            "created_at"
        )
        extra_kwargs = {"password": {"write_only": True}}

