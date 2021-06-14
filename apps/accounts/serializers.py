from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth import authenticate

User = get_user_model()


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'password',)

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'])
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')


class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid Details.")