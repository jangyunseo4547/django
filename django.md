## 0. 웹 프레임 워크
- 장고 : 파이썬 기반의 웹 프레임 워크
![장고 프레임워크](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/MVC-Process.svg/300px-MVC-Process.svg.png)
    - MTV : 장고에서 부르는 MVC를 뜻함. 
    - MVC : 모델(데이터 베이스) - 뷰(HTML) - 컨트롤러(동작 : 파이썬)


### MTV
- client ---> request(127.0.0.1:8000<path>/<path2>) 
- => 1) urls.py => 2) views.py => 3) models.py => 4) template(HTML) -> view.py ----> response(html)

- MTV
    - M : models.py
    - T : templates
    - V : views.py