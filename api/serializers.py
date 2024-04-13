from rest_framework import serializers 
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import * 
 
 
class UserSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = CustomUser 
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password'] 

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_user(self, username):
        return CustomUser.objects.get(username=username)
 
class StudentSerializer(serializers.ModelSerializer): 
    user = UserSerializer() 
 
    class Meta: 
        model = Student 
        fields = ['id', 'user', 'join_date', 'last_login'] 
 
 
class TeacherSerializer(serializers.ModelSerializer): 
    user = UserSerializer() 
 
    class Meta: 
        model = Teacher 
        fields = ['id', 'user', 'join_date', 'last_login'] 
 
 
class MockTestResultSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = MockTestResult 
        fields = '__all__' 
 
 
class LearningActivitySerializer(serializers.ModelSerializer): 
    class Meta: 
        model = LearningActivity 
        fields = '__all__' 
 
class MockTestSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = MockTest 
        fields = '__all__'

class TipsHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TipsHistory
        fields = '__all__'