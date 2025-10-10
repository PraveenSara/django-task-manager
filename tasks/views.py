from django.shortcuts import render, redirect
from .models import Task
# Create your views here.

def home(request):
    tasks = Task.objects.all().order_by('-id')
    return render(request, 'tasks/home.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
    return redirect('home')

def delete_task(request, task_id):
    Task.objects.filter(id=task_id).delete()
    return redirect('home')

def toggle_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('home')
