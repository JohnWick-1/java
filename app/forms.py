from django import forms
from .models import *


class StudentForm(forms.ModelForm):
    name = forms.CharField(max_length=20)
    math = forms.IntegerField()
    eng = forms.IntegerField()
    phy = forms.IntegerField()
    avg = forms.FloatField()

    class Meta:
        model = Student

class StudentData(forms.ModelForm):
    photo = forms.ImageField(upload_to='DataStorage/Images/% Y/% m/% d/', height_field=None, width_field=None, max_length=100)
    file = forms.FileField(upload_to='DataStorage/FileStore/% Y/% m/% d/')

    class Meta:
        model = StudentData