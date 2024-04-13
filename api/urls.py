from django.urls import path 
from .views import * 
 
 
urlpatterns = [ 
    # URLs for Student 
    path('token/', CustomTokenObtainPairView.as_view(), name='student_token_obtain_pair'), 
    path('sign-up/', RegisterAPIView.as_view(), name='sign-up'),
    path('students/', StudentListCreateAPIView.as_view(), name='student-list'), 
    path('students/<int:pk>/', StudentRetrieveUpdateDestroyAPIView.as_view(), name='student-detail'), 
     
    path('teachers/', TeacherListCreateAPIView.as_view(), name='teacher-list'), 
    path('teachers/<int:pk>/', TeacherRetrieveUpdateDestroyAPIView.as_view(), name='teacher-detail'), 
 
    path('mocktestresults/', MockTestResultCreateAPIView.as_view(), name='mocktestresult-list'), 
    path('mocktestresults/', MockTestResultListAPIView.as_view(), name='mocktestresult-list'), 
    path('mocktestresults/<int:pk>/', MockTestResultRetrieveUpdateDestroyAPIView.as_view(), name='mocktestresult-detail'), 
 
    path('learningactivities/', LearningActivityCreateAPIView.as_view(), name='learningactivity-list'), 
    path('learningactivities/', LearningActivityListAPIView.as_view(), name='learningactivity-list'), 
    path('learningactivities/<int:pk>/', LearningActivityRetrieveUpdateDestroyAPIView.as_view(), name='learningactivity-detail'), 
 
    path('mocktests/', MockTestListCreateAPIView.as_view(), name='mocktest-list'), 
    path('mocktests/<int:pk>/', MockTestRetrieveUpdateDestroyAPIView.as_view(), name='mocktest-detail'), 
]