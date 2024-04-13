from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'student'),
        ('parent', 'parent'),
        ('techer', 'techer')
        ('teacher', 'teacher')
    )
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')

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
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    teachers = models.ManyToManyField(Teacher)


class IELTSTest(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    reading_score = models.FloatField()
    listening_score = models.FloatField()
    speaking_score = models.FloatField()
    writing_score = models.FloatField()
    participant_id = models.ForeignKey(Student, on_delete=models.CASCADE)


    