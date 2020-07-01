from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=20)
    math = models.IntegerField()
    eng = models.IntegerField()
    avg = models.FloatField()

    def __str__(self):
        return self.name


class StudentData(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='DataStorage/Images/% Y/% m/% d/', height_field=None, width_field=None, max_length=100)
    file = models.FileField(upload_to='DataStorage/FileStore/% Y/% m/% d/')


class UserEdit(models.Model):
    user = User()
    pass

