from rest_framework import serializers 
from .models import * 
 
 
class UserSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = User 
        fields = ['id', 'username', 'email', 'first_name', 'last_name'] 
 
 
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