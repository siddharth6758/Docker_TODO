from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo

def index(request):
    todos = Todo.objects.order_by('-created_at')
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Todo.objects.create(title=title)
        return redirect('index')
    return render(request, 'index.html', {'todos': todos})

def toggle(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.completed = not todo.completed
    todo.save()
    return redirect('index')

def delete_item(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect('index')
