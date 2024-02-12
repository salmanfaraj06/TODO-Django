# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import TodoItem
from .forms import TodoForm

def home(request):
    todos = TodoItem.objects.all()
    return render(request, 'home.html', {'todos': todos})

def todos(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TodoForm()
    todos = TodoItem.objects.all()
    return render(request, 'todos.html', {'todos': todos, 'form': form})

def delete_todo(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('todos')
    return render(request, 'confirm_delete.html', {'todo': todo})


def edit_todo(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todos')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'edit_todo.html', {'form': form})