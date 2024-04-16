from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('delete/<int:todo_id>/', views.todo_delete, name='todo_delete'),
]