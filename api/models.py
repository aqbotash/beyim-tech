from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission
# Create your models here.


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'student'),
        ('parent', 'parent'),
        ('teacher', 'teacher')  # Fixed typo in role choice
    )
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')
    groups = models.ManyToManyField(Group, related_name='custom_users')  # Added related_name argument
    user_permissions = models.ManyToManyField(Permission, related_name='custom_users')  # Added related_name argument

    def __str__(self):
        return self.username

class Teacher(CustomUser):
    lessons = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Parent(CustomUser):
    payments = models.FloatField()
    def __str__(self):
        return self.name

class Student(CustomUser):
    guardian = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name='students')
    teachers = models.ManyToManyField(Teacher)


class IELTSTest(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    reading_score = models.FloatField()
    listening_score = models.FloatField()
    speaking_score = models.FloatField()
    writing_score = models.FloatField()
    participant_id = models.ForeignKey(Student, on_delete=models.CASCADE)


class Activity(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    name = models.CharField(max_length=100)
    participants = models.ManyToManyField(Student)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    