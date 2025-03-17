from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html') # HTML 문서를 가져와서 렌더링

def hello():
    pass
