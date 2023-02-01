from django.urls import path

from todo_list_app import views
from todo_list_app.views import todo_task_create, todo, TodoSearch

urlpatterns = [
    path('create/', todo_task_create),
    path('<int:pk>', todo),
    path('all/', TodoSearch.as_view())

]

