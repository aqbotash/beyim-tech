from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer, IELTSTestSerializer
from .models import IELTSTest
from rest_framework.response import Response

class RegisterAPIView(generics.CreateAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        password = serializer.validated_data['password']
        user = User.objects.create_user(
            username=serializer.validated_data['username'],
            email=serializer.validated_data['email'],
            password=password, 
        )
        return user
    
# For creating and taking fake an IELTS tests for students  
class IELTSTestAPIView(generics.ListCreateAPIView):
    queryset = IELTSTest.objects.all()
    serializer_class = IELTSTestSerializer
    
    def get(self, request, *args, **kwargs):
        user_id = self.request.user.id
        tests = self.queryset.filter(user_id=user_id)
        serializer = self.get_serializer(tests, many=True)
        return Response(serializer.data)
    
    