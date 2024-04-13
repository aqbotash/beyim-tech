from django.contrib.auth.models import User
from rest_framework import serializers
from .models import IELTSTest


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email', 'password']
        extra_kwargs = {
            'password': {'write_only': True},  # Ensure password is write-only
        }


class IELTSTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = IELTSTest
        fields = '__all__'
        
