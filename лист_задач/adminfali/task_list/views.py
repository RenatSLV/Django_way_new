from django.shortcuts import render, redirect
from task_list.models import *

# Create your views here.
def get_all(request):
    AllTask = Task.objects.all()
    return render(request,'alltask.html', {'AllTask': AllTask})

def add_task(request):
    if request.method == 'POST':
        obj = Task(task=request.POST['task'],
                   taskInfo=request.POST['taskInfo'])
        obj.save()
        return redirect('get_all')
    return render(request, 'addtask.html')

def delet_task_by_id(request):
    if request.method == 'POST':
        obj = Task.objects.filter(id=request.POST['id']).delete()
        return redirect('get_all')
    return render(request, 'deleteTask.html')