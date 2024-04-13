from django.db import models

# Create your models here.
class IELTSTest(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    reading_score = models.FloatField()
    listening_score = models.FloatField()
    speaking_score = models.FloatField()
    writing_score = models.FloatField()
    participant_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    

    