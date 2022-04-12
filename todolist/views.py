from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import Todolist
from .forms import TodoListForm
# Create your views here.


def index(request):
    todo_items = Todolist.objects.order_by('id')
    form = TodoListForm()
    context = {'todo_items': todo_items, 'form': form}
    return render(request, 'todolist/index.html', context)


@require_POST
def add_todo(request):
    form = TodoListForm(request.POST)
    if form.is_valid():
        new_todo = Todolist(text=request.POST['text'])
        new_todo.save()

    return redirect('index')


def completed_todo(request, todo_id):
    todo = Todolist.objects.get(pk=todo_id)
    todo.completed = True
    todo.save()

    return redirect('index')


def delete_completed(request):
    Todolist.objects.filter(completed__exact=True).delete()
    return redirect('index')


def delete_all(request):
    Todolist.objects.all().delete()
    return redirect('index')
