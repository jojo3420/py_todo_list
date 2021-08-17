from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('newTodo/', views.new_todo, name='new_todo'),
    path('deleteTodo/', views.delete_todo, name='delete_todo')
]