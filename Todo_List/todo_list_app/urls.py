from django.urls import path

from todo_list_app import views
from todo_list_app.views import todo_task, todo_task_create, todo

urlpatterns = [
    path('all/', todo_task),
    path('create/', todo_task_create),
    path('<int:pk>', todo),

]

