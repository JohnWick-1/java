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
    print(request.__dict__)
    if request.method == 'POST' and request.FILES:
        print('inside if ---save form----')
        context = {'msg': 'Data has saved'}
        # print(request.POST['name'])
        # print(request.POST['math'])
        # print(request.POST['eng'])
        # print(request.POST['phy'])
        # print(request.POST['avg'])
        # print(request.FILES['image'])
        # print(request.FILES['document'])
        # print(request.FILES['photo'])

        stud_form = StudentForm(request.POST, request.FILES,instance=Student())

        print(22 * '*')
        if stud_form.is_valid():
            print('student valid')
            # stud_form.save()
            print(stud_form.__dict__)
            print('_'*40)
            print(stud_form.instance)
            print(id(stud_form))
            if isinstance(stud_form, Student):
                print("stud_form is my object")
            print('@'*40)
        studData_form = StudentDataForm(request.POST, request.FILES,instance=StudentData())
        if studData_form.is_valid():
            print('image valid')
            x = studData_form.save(commit=False)
            # x.student = stud_form
            # x.student = StudentForm(request.POST, request.FILES,instance=Student())
            stud = Student(name=request.POST['name'],
                           math=request.POST['math'],
                           eng=request.POST['eng'],
                           phy=request.POST['phy'],
                           avg=request.POST['avg'],
                           img=request.FILES['img'],
                           doc=request.FILES['doc'])
            stud.save()
            x.student = stud
            print(x.__dict__)
            x.save()
    return redirect(reverse('showform'))

