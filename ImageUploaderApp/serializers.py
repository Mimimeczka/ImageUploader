from .models import User, AccountType, Image
from rest_framework import serializers


class AccountTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountType
        fields = ['types']


class ImageTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['user_id']


class UserSerializer(serializers.ModelSerializer):
    account_type = AccountTypeSerializer(many=False)
    images_links = ImageTypeSerializer(many=True)

    class Meta:
        model = User
        fields = ['mail', 'account_type', 'images_links']