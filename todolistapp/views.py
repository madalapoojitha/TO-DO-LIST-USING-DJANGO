from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def index(request):
    tasks = Task.objects.filter(completed=False) 
    completed_tasks = Task.objects.filter(completed=True)
    return render(request, 'frontend.html', {'tasks': tasks, 'completed_tasks': completed_tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        due_date = request.POST['due_date']
        priority = request.POST['priority']
        Task.objects.create(title=title, due_date=due_date, priority=priority)
        return redirect('index')

def remove_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect('index')

def mark_as_completed(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.completed = True
    task.save()
    return redirect('index')  
