from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Todo


# Create your views here.


def index(req):
    # return HttpResponse('hello world')
    todos = Todo.objects.all()
    # print(todos)
    data = {'todos': todos}
    return render(req, 'todo_app/index.html', data)


def add_todo(req):
    content = req.POST['content']
    print(f'content: {content}')
    new_todo = Todo(content=content)
    new_todo.save()
    return HttpResponseRedirect(reverse('index'))


def delete_todo(req):
    id = req.GET['id']
    # print(f'id: {id}')
    todo = Todo.objects.get(id=id)
    todo.delete()
    # return HttpResponse('delete todo')
    return HttpResponseRedirect(reverse('index'))
