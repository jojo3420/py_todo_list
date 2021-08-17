from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Todo


# Create your views here.


def index(req):
    # return HttpResponse('hello world')
    todos = Todo.objects.all().filter(is_done=False)
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
    ## todo.delete()

    # 첫번째 방법 - 인스턴스
    # todo = Todo.objects.get(id=id)
    # print(f'todo type {type(todo)}')  # <class 'todo_app.models.Todo'>
    # if todo:
    #     todo.is_done = True
    #     todo.save()

    # 두번째 방법 - querySet
    querySet = Todo.objects.filter(id=id)
    # print(type(querySet)) # <class 'django.db.models.query.QuerySet'>
    querySet.update(is_done=True)
    # return HttpResponse('delete todo')
    return HttpResponseRedirect(reverse('index'))
