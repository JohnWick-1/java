from django.shortcuts import render, reverse, redirect
from .models import *
from .forms import *
# Create your views here.

count = 1
def show(request):
    global count
    context = {'msg':'Home Page'}
    print('count in show = ', count)
    count+=1
    return render(request,'app/form.html', context)

def save(request):
    print('count in save = ', count)
    print('here-------------')
    context = {'msg':'Data not saved'}
    print(request.__dict__)
    if request.method == 'POST' and request.FILES:
        context = {'msg': 'Data has saved'}
        print(request.POST['name'])
        print(request.POST['math'])
        print(request.POST['eng'])
        print(request.POST['phy'])
        print(request.POST['avg'])
        print(request.FILES['image'])
        print(request.FILES['document'])
        print(request.FILES['photo'])

        stud = Student(name = request.POST['name'],
                math = request.POST['math'],
                eng =  request.POST['eng'],
                phy=request.POST['phy'],
                avg = request.POST['avg'],
                img = request.FILES['image'],
                doc = request.FILES['document'])
        print(stud.__dict__)
        print(22*'*')
        stud.save()
        studData = StudentData(student = stud, photo = request.FILES['photo'])
                # file = request.FILES['file1'])
        print(studData.__dict__)
        try:
            print('-in try......')
            studData.save()
        except Exception as e:
            print('---in except------')
            print("Error is--",e)
            stud.delete()
    return redirect(reverse('index'))

def showForm(request):
    global count
    print('count in showForm= ', count)
    count+=1
    studform = StudentForm()
    studDataform = StudentDataForm()
    context = {'msg': 'Home Page in showForm', 'studform':studform, 'studDataform':studDataform}
    return render(request,'app/studform.html', context)

def saveForm(request):
    print('count in saveForm = ', count)
    print('here--saveForm-----------')
    context = {'msg':'Data not saved'}
    # print(request.__dict__)
    if request.method == 'POST' and request.FILES:
        print('inside if ---save form----')
        context = {'msg': 'Data has saved'}
        print(request.POST['name'])
        print(request.POST['math'])
        print(request.POST['eng'])
        print(request.POST['phy'])
        print(request.POST['avg'])
        # print(request.POST[''])
        stud_form = StudentForm(request.POST, request.FILES)
        if stud_form.is_valid():
            print('student valid')
            stud_form.save(commit=False)
        studData_form = StudentDataForm(stud_form, request.POST, request.FILES)
        if studData_form.is_valid():
            print('image valid')
            print(studData_form.__dict__)
            studData_form.save()
    return redirect(reverse('showform'))

