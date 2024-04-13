from django.db import models 
from django.contrib.auth.models import AbstractUser 
from django.contrib.auth.models import Group, Permission 
 
class CustomUser(AbstractUser): 
    groups = models.ManyToManyField(Group, related_name='api_users') 
    user_permissions = models.ManyToManyField(Permission, related_name='api_users') 
    is_student = models.BooleanField(default=False) 
    is_teacher = models.BooleanField(default=False) 
 
class Student(models.Model): 
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE) 
    debts = models.DecimalField(max_digits=5, decimal_places=2) 
    join_date = models.DateField(auto_now_add=True) 
    last_login = models.DateTimeField(auto_now=True) 
 
class Teacher(models.Model): 
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE) 
    per_hour_fees = models.DecimalField(max_digits=5, decimal_places=2) 
    students = models.ManyToManyField(Student, related_name='teachers', default=None) 
    join_date = models.DateField(auto_now_add=True) 
    last_login = models.DateTimeField(auto_now=True) 
 
 
# Teachers first add mock tests and then add students to the mock tests 
class MockTest(models.Model): 
    name = models.CharField(max_length=255) 
    id = models.IntegerField(primary_key=True) 
    test_date = models.DateField() 
 
     
class MockTestResult(models.Model): 
    student = models.ForeignKey(Student, on_delete=models.CASCADE) 
    mock_test = models.ForeignKey('MockTest', on_delete=models.CASCADE) 
    listening_score = models.DecimalField(max_digits=5, decimal_places=2) 
    reading_score = models.DecimalField(max_digits=5, decimal_places=2) 
    writing_score = models.DecimalField(max_digits=5, decimal_places=2) 
    speaking_score = models.DecimalField(max_digits=5, decimal_places=2) 
    overall_band_score = models.DecimalField(max_digits=5, decimal_places=2) 
 
class LearningActivity(models.Model): 
    name = models.CharField(max_length=100)
    description = models.TextField() 
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE) 
    duration = models.DurationField() 
    # teachers will add them 
    students = models.ManyToManyField(Student, related_name='learning_activities')

class TipsHistory(models.Model):
    user_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    text = models.TextField()