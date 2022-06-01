from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import Todolist
from .forms import TodoListForm

# Create your views here.


def index(request):
    """
    Rendering Index page
    """
    todo_items = Todolist.objects.order_by("id")
    form = TodoListForm()
    context = {"todo_items": todo_items, "form": form}
    return render(request, "todolist/index.html", context)


@require_POST
def add_todo(request):
    """
    add to do post request
    """
    form = TodoListForm(request.POST)
    if form.is_valid():
        new_todo = Todolist(text=request.POST["text"])
        new_todo.save()

    return redirect("index")


def completed_todo(request, todo_id):
    """
    Completed to do function
    returns: redirect to index page
    """
    todo = Todolist.objects.get(pk=todo_id)
    todo.completed = True
    todo.save()

    return redirect("index")


def delete_completed(request):
    """
    deletes the completed task and redirects to index
    returns: redirect to index home page
    """
    Todolist.objects.filter(completed__exact=True).delete()
    return redirect("index")


def delete_all(request):
    """
    deletes all tasks and redirects to index
    returns: redirects to index homepage
    """
    Todolist.objects.all().delete()
    return redirect("index")
