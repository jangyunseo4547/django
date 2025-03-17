# Django


## 0. setting

- `.gitignore`
- 가상환경 설정 
    - python -m venv venv
    - source venv/Scripts/activate
- `README.md` 

## 1. Django 프로젝트 
1. django 설치
```shell (터미널 창에서 쓰는 명령어)
pip install django
```

## 2. 프로젝트 생성 명령어
```shell
django-admin startproject <pjt-name> <path> : django-admin startproject first_pjt .
```

## 3. 서버 실행 (서버 종료 : ctrl + c)
```shell
python manage.py runserver
```
- `http://127.0.0.1:8000/` : ctrl + 클릭 
    - 127 : 내 컴퓨터에 요청을 보냄 
    - 8000 : 포트 번호 (장고는 일반적으로 8000 사용 )


## 4. 앱 생성
```shell
django-admin startapp <app-name> :  
```
- first_app : 프로젝트를 담당하는 모듈을 뜻함.

## 5. 앱 등록 (`settings.py`)
```python
INSTALLED_APPS = [
    ...,
    '<app_name>',
]
```
- INSTALLED_APPS =에 'first_app', 쓰기


## 6. MTV 과정 
- 6.1 
### 1) (`urls.py`) 불러오기
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('hello/', views.hello),  
```
### 2) first_app에 (`templetes`) 폴더 만들기

### 3) (`views.py`) 선언하기
```python
def index(request):
    return render(request, 'index.html')

def hello():
    pass
```
- `127.0.0.1:8000/index/`로 접근

- 6.2 
### (`views.py`)
```python
def hello(request):
    my_name = 'changhee'

    context = {
        'my_name': my_name,
    }
    return render(request, 'hello.html', context)
```

### (`templetes` - `hello.html`)
`<h1>안녕하세요 {{my_name}}입니다.</h1>`


### articles.html
- 6-3
```shell
<body>
    <h1 style="color: red">articles</h1>
    {% for fake_article in fake_articles %} # 파이썬 방식 
        <p>{{fake_article}}</p>
    {% endfor %}  # {% %} : if, for 등 임의의 로직을 실행하기 위해 쓰이는 태그
</body>
```
 #### 부트 스트랩 활용
    - head 끝나기 전 : 붙여넣기
    - body 끝나기 전 : 붙여넣기

- 들여쓰기 
```shell
<div class="container"> # div.container + tab
        <h1 style="color: red">articles</h1>
        {% for fake_article in fake_articles %}
            <p>{{fake_article}}</p> # --> <div class="alert alert-light">{{fake_article}}</div> 바꿔주기 
        {% endfor %} # alt + 위 화살표로 div안에 넣어주기
    </div>
```
