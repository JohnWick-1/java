from django import forms
from .models import *


class StudentForm(forms.ModelForm):
    # name = forms.CharField(max_length=20)
    # math = forms.IntegerField()
    # eng = forms.IntegerField()
    # phy = forms.IntegerField()
    # avg = forms.FloatField()

    class Meta:
        model = Student
        fields = "__all__"

class StudentDataForm(forms.ModelForm):
    # student = forms.ModelChoiceField(queryset=Student.objects.last())
    # photo = forms.ImageField(upload_to='images/% Y/% m/% d/')
    # # file = forms.FileField(upload_to='images/% Y/% m/% d/')

    class Meta:
        model = StudentData
        fields = ("photo",)
        # fields = "__all__"
