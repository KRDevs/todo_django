from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import NewTask
from .models import Task

@login_required
def tasks(request):
    return render(request,'task/tasks.html')
@login_required
def detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    is_author = request.user == task.author
    return render(request, 'task/detail.html', {
        'task': task,
        'is_author': is_author
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
