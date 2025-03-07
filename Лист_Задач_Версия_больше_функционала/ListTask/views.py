from django.shortcuts import render, redirect
from ListTask.models import *
# Create your views here.
#     ____   ______ _   __ ___       _____  __  _    __
#    / __ \ / ____// | / //   |     / ___/ / / | |  / /
#   / /_/ // __/  /  |/ // /| |     \__ \ / /  | | / / 
#  / _, _// /___ / /|  // ___ |    ___/ // /___| |/ /  
# /_/ |_|/_____//_/ |_//_/  |_|   /____//_____/|___/   
                                                     
def get_all(request):
    AllTask = Task.objects.all()
    context = {'Alltask': AllTask}
    return render(request, 'all_task.html', context)

def add_task(request):
    if request.method == "POST":
        obj = Task(Task=request.POST['Task'],
                    Task_Info=request.POST['Task_Info'])
        obj.save()
        return redirect('get_all')
    return render(request, 'add_task.html')

def delet_task_by_id(request):
    if request.method == 'POST':
        obj = Task.objects.filter(id=request.POST['id']).delete()
        return redirect('get_all')
    return render(request, 'delete_task.html')

def get_one_task_by_id(request):
    context = {}
    if request.method == 'POST':
        taskID = request.POST.get('id')
        obj = Task.objects.get(id=taskID)
        context['obj'] = obj
    return render(request, 'get_one_task.html', context)