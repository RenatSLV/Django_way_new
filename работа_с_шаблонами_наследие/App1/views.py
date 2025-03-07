from django.shortcuts import render, redirect
from App1.models import Todo

def list_todos(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'base.html', context)

def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        status = request.POST.get('status')

        Todo.objects.create(title=title, status=status)
        return redirect('list')
    return render(request, 'add_todo.html')

def delete_todo(request, id):
    if request.method == 'POST':
        todo = Todo.objects.filter(id=id).delete()
        context = {
            'id': id
        }
        return redirect('list')
    return render(request, 'delete.html')

def detail_todo(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        'todo': todo
    }
    return render(request, 'detail.html', context)
