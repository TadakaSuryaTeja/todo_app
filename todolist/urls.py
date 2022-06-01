from django.urls import path

from todolist import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add_todo, name="add"),
    path("completed/<todo_id>", views.completed_todo, name="completed"),
    path("deletecomplete", views.delete_completed, name="deletecomplete"),
    path("deleteall", views.delete_all, name="deleteall"),
]
