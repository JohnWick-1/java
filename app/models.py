from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=20)
    math = models.IntegerField()
    eng = models.IntegerField()
    avg = models.FloatField()

    def __str__(self):
        return self.name
