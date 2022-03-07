from django.db import models

# Create your models here.

class Info(models.Model):
    name=models.CharField(max_length=40)
    age=models.IntegerField()
    stack=models.CharField(max_length=30)
    exp=models.IntegerField()
    proficiency=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

