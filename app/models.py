from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=20)
    math = models.IntegerField()
    eng = models.IntegerField()
    phy = models.IntegerField()
    avg = models.FloatField()
    img = models.ImageField(upload_to='images/%Y/%m/%d', blank=True, null=True)
    doc = models.FileField(upload_to='documents/%Y/%m/%d')

    def __str__(self):
        return self.name


class StudentData(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='images/%Y/%m/%d', blank=True, null=True)
    # file1 = models.FileField(upload_to='documents/%Y/%m/%d')


class UserEdit(models.Model):
    user = User()
    pass

