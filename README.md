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

Model 
---
### model.py 모델 정의 
```python
from django.db import models

class MyTableModel(models.Model):
    some_field = models.CharField(max_length=256)
    others_field = models.IntegerField()
```


### 최초 마이그레이션 생성하기
migrations 디렉터리에 0001_inital.py 마이그레이션 생성됨
이 명령어는 실제 db 에 적용하는 migration을 생성하고 이 마이그레이션은 청사진 또는 설계도 역활을 함

```shell
python manage.py makemigrations
```


### 마이그레이션 DB에 적용하기
파이썬의 기본 테이블 생성가 개발자가 정의한 클래스가 DB 테이블로 생성 된다. 
테이블 이름 규칙은 앱이름_클래스이름
ex) my_todo_app_todo 형식으로 이름 지어짐

```shell
python manage.py migrate
```






