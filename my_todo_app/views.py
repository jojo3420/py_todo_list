from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    # return HttpResponse('hello world')
    return render(request, 'my_todo_app/index.html')