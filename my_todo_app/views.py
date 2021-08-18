from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *


# Create your views here.
def index(request):
    # return HttpResponse('hello world')
    # todos = Todo.objects.all()
    todos = Todo.objects.filter(is_done=False)
    data = {'todos': todos}
    return render(request, 'my_todo_app/index.html', data)


def new_todo(request):
    content = request.POST['todo_content']
    # print(content)
    todo = Todo(content=content)
    todo.save()
    # return HttpResponse('신규 메모 작성: ' + content)
    return HttpResponseRedirect(reverse('index'))


def done_todo(request):
    id = request.GET['id']
    # print(f'id: {id}')
    todo = Todo.objects.get(id=id)
    # todo.delete()

    # 첫번째 방법
    if todo:
        todo.is_done = True
        todo.save()

    # 두번째 방법
    # query_set = Todo.objects.filter(id=id).update(id_done=True)
    return HttpResponseRedirect(reverse('index'))
