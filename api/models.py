from django.db import models
from django.contrib.auth.models import AbstractUser

class CostomUser(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'student'),
        ('parent', 'parent'),
        ('techer', 'techer')
    )
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')
    
    def __str__(self):
        return self.username

