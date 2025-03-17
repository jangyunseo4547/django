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
### (`urls.py`) 불러오기
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('hello/', views.hello),  
```
### first_app에 (`templetes`) 폴더 만들기

### (`views.py`) 선언하기
```python
def index(request):
    return render(request, 'index.html')

def hello():
    pass
```
- `127.0.0.1:8000/index/`로 접근