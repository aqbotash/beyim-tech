from django.contrib import admin 
from .models import * 
 
admin.site.register(Student) 
admin.site.register(CustomUser) 
admin.site.register(Teacher) 
admin.site.register(MockTestResult) 
admin.site.register(LearningActivity) 
admin.site.register(MockTest)
admin.site.register(TipsHistory)