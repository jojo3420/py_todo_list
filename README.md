# py_todo_list
Django 한그릇 뚝닥  Todo List App

1> 앱 만들기
```
python manage.py startapp 앱이름
```


2> settings.py 앱추가 
 INSTALLED_APPS 배열안에 앱이름 문자열 추가 
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'my_todo_app',  # 앱추가
]
```

3> 최상위 urls.py 에 my_todo_app urls.py 연결 
"127.0.0.1:8000" 즉 '' 경로로 http 요청이 들어올 때 my_todo_app 응답 하도록 연결
```angular2html
from django.urls import path, include

path('', includes('my_todo_app.urls'))
```
1) import 문에 include 추가 
2) path 함수에 연결 


4> my_todo_app urls.py 파일 생성 후 views.py 연결 
```angular2html
from . import views 
urlspatterns = [
  path('', views.index)
]
```

5> views.py index 핸들러 함수 생성
```
from django.http import HttpResponse 
def index(request):
  return HttpResonse('hello world')

```
