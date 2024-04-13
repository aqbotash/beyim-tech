from rest_framework import generics
from .models import * 
from .serializers import * 
from .permissions import * 
from rest_framework.permissions import IsAuthenticated 
from .permissions import IsStudent, IsTeacher 
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from openai import OpenAI

client = OpenAI(api_key='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')
# import environ

# env = environ.Env()


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class RegisterAPIView(generics.CreateAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        password = serializer.validated_data['password']
        user = CustomUser.objects.create_user(
            username=serializer.validated_data['username'],
            email=serializer.validated_data['email'],
            password=password, 
        )
        return user

def prompt_giver(input_file, replacements):
        prompt_dictionary = {}

        with open(input_file, 'r') as input_file:
            modified_content = input_file.read()
            for target_string, replacement_string in replacements.items():
                modified_content = modified_content.replace(target_string, replacement_string)

            prompt_dictionary["user"] = modified_content

        return prompt_dictionary["user"]

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

    def post(self, request, *args, **kwargs):
        post_serializer = self.get_serializer(data=request.data)
        if post_serializer.is_valid():
            student_id = post_serializer.validated_data['student']
            post_serializer.save()

        tests = self.queryset.filter(student=student_id)
        get_serializer = self.get_serializer(tests, many=True)
        list_of_data = get_serializer.data
        replacements = {}
        indx = len(list_of_data)
        if(indx >= 5):
            for i in range(5):
                replacements[f'listening_score{i + 1}'] = list_of_data[indx - i - 1]['listening_score'] 
                replacements[f'reading_score{i + 1}'] = list_of_data[indx - i - 1]['reading_score'] 
                replacements[f'speaking_score{i + 1}'] = list_of_data[indx - i - 1]['speaking_score'] 
                replacements[f'writing_score{i + 1}'] = list_of_data[indx - i - 1]['writing_score']

            prompt = prompt_giver('api/prompt.txt', replacements)
            
            chat_response = client.chat.completions.create(model = "gpt-3.5-turbo",
            messages = [
                    {"role": "user", "content": prompt},
                    ])
            assistant_reply = chat_response.choices[0].message.content
            
            tipsHistorySerializer = TipsHistorySerializer(data={'user_id': student_id.id, 'text': str(assistant_reply)})
            
            if tipsHistorySerializer.is_valid():
                print('valid')
                tipsHistorySerializer.save()

        return Response(post_serializer.data)

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