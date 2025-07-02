from django.db import models

# Create your models here.
class student(models.Model):
    rollno = models.IntegerField()
    name=models.CharField(max_length=100)
    marks=models.IntegerField()
    add=models.models.CharField(max_length=50)
    