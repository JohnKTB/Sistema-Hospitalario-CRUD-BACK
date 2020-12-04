from django.contrib.auth.models import Permission
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from applications.users.models import User


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def get_token(self, user):
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        # ...
        return token


class RolSerializer(serializers.SerializerMethodField):
    class Meta:
        fields = '__all__'


class permisosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'


class userListaSerializer(serializers.ModelSerializer):
    user_permissions = permisosSerializer(many=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'password',
            'rol',
            'is_staff',
            'user_permissions',
            'is_superuser',
            'email',
        )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class ArrayPermisosSerializer(serializers.ListField):
    permisos = serializers.CharField()


class createUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'is_staff',
            'user_permissions',
            'is_superuser',
            'email',
        )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

