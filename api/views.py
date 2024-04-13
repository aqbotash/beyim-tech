from rest_framework import generics 
from .models import * 
from .serializers import * 
from .permissions import * 
from rest_framework.permissions import IsAuthenticated 
from .permissions import IsStudent, IsTeacher 
from rest_framework import generics 
from .models import * 
from .serializers import * 
from .permissions import * 
from rest_framework.permissions import IsAuthenticated 
from .permissions import IsStudent, IsTeacher 
     
class StudentListCreateAPIView(generics.ListCreateAPIView): 
    queryset = Student.objects.all() 
    serializer_class = StudentSerializer 
 
 
class StudentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Student.objects.all() 
    serializer_class = StudentSerializer 
 
 
class TeacherListCreateAPIView(generics.ListCreateAPIView): 
    queryset = Teacher.objects.all() 
    serializer_class = TeacherSerializer 
 
 
class TeacherRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Teacher.objects.all() 
    serializer_class = TeacherSerializer 
 
 
class MockTestResultListAPIView(generics.ListAPIView): 
    queryset = MockTestResult.objects.all() 
    serializer_class = MockTestResultSerializer 
    permission_classes = [IsAuthenticated, IsTeacher, IsStudent] 
     
     
     
class MockTestResultCreateAPIView(generics.CreateAPIView): 
    queryset = MockTestResult.objects.all() 
    serializer_class = MockTestResultSerializer 
    permission_classes = [IsAuthenticated, IsTeacher] 
 
class MockTestResultRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView): 
    queryset = MockTestResult.objects.all() 
    serializer_class = MockTestResultSerializer 
    permission_classes = [IsAuthenticated, IsTeacher] 
 
 
 
# split the MockTestResultListCreateAPIView into two separate views 
class LearningActivityListAPIView(generics.ListCreateAPIView): 
    queryset = LearningActivity.objects.all() 
    serializer_class = LearningActivitySerializer 
    permission_classes = [IsAuthenticated] 
 
    def get_queryset(self): 
        user = self.request.user 
        if user.is_teacher: 
            return MockTestResult.objects.filter(teacher=user) 
        elif user.is_student: 
            return MockTestResult.objects.filter(students=user) 
        else: 
            return MockTestResult.objects.none() 
         
         
class LearningActivityCreateAPIView(generics.ListCreateAPIView): 
    queryset = LearningActivity.objects.all() 
    serializer_class = LearningActivitySerializer 
    permission_classes = [IsAuthenticated, IsTeacher] 
 
 
class LearningActivityRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView): 
    queryset = LearningActivity.objects.all() 
    serializer_class = LearningActivitySerializer 
    permission_classes = [IsAuthenticated] 
 
 
 
 
class MockTestListCreateAPIView(generics.ListCreateAPIView): 
    queryset = MockTest.objects.all() 
    serializer_class = MockTestSerializer 
    permission_classes = [IsAuthenticated, IsTeacher] 
 
 
class MockTestRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView): 
    queryset = MockTest.objects.all() 
    serializer_class = MockTestSerializer 
 
 
 
#  View for teachers amount of salary 
 
# счет permission_classes = [IsStudentPermission] - для студентов