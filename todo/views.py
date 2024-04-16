from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Todo_Item

def todo_list(request):
    if request.method == 'POST':
        todo = request.POST.get('todo')
        Todo_Item.objects.create(todo=todo)
        return redirect('todo:todo_list')
    
    todo = Todo_Item.objects.all()
    context={'todo' : todo}
    return render(request, 'todo/todo_list.html', context)

def todo_delete(request, todo_id):
    todo = Todo_Item.objects.get(pk=todo_id)
    todo.delete()
    return redirect('todo:todo_list')



