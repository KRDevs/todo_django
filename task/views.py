from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import NewTask, EditTask
from .models import Task, List


@login_required
def lists(request):
    lists = List.objects.all()
    tasks = Task.objects.all()
    return render(request, 'task/lists.html', {
        'lists': lists,
        'tasks': tasks,
    })


@login_required
def list_table(request, pk):
    list = get_object_or_404(List, pk=pk)
    tasks = Task.objects.filter(list=list)
    return render(request, 'task/list_table.html', {
        'list': list,
        'tasks': tasks
    })


@login_required
def tasks(request):
    tasks = Task.objects.filter(is_complete=False)
    list_id = request.GET.get('list', 0)
    count = Task.objects.all().count()
    return render(request, 'task/tasks.html', {
        'tasks': tasks,
        'list_id': int(list_id),
        'count': count
    })


@login_required
def detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    is_author = request.user == task.author
    list_id = request.GET.get('list', 0)
    lists = List.objects.all()
    return render(request, 'task/detail.html', {
        'task': task,
        'is_author': is_author,
        'list_id': int(list_id),
        'lists': lists
    })


@login_required
def new_task(request):
    if request.method == 'POST':
        form = NewTask(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.save()
            return redirect('task:detail', pk=task.id)
    else:
        form = NewTask()
        return render(request, 'task/new_task.html', {
            'form': form,
            'title': 'Add new task'
        })


@login_required
def delete(request, pk):
    task = get_object_or_404(Task, pk=pk, author=request.user)
    task.delete()
    return redirect('task:tasks')


@login_required
def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk, author=request.user)
    if request.method == 'POST':
        form = EditTask(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task:detail', pk=task.id)
    else:
        form = EditTask(instance=task)
    return render(request, 'task/new_task.html', {
        'form': form,
        'title': 'Edit task'
    })
