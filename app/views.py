from django.shortcuts import render, reverse, redirect
from .models import *
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
    # print(request.__dict__)
    if request.method == 'POST':
        context = {'msg': 'Data has saved'}
        print(request.POST['name'])
        print(request.POST['math'])
        print(request.POST['eng'])
        # print(request.POST[''])
        # stud = Student()
    return redirect(reverse('index'))
