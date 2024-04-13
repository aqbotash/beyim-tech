from django.contrib.auth.models import User
from rest_framework import serializers
from .models import IELTSTest, CustomUser, Activity, Student


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username','email', 'password', 'category']
        extra_kwargs = {
            'password': {'write_only': True},  # Ensure password is write-only
        }


class IELTSTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = IELTSTest
        fields = '__all__'


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'        