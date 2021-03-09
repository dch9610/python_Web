# __파이썬 웹 프로그래밍__
<br>

# 목차
## [1.목적](#목적)
## [2.개발환경](#개발환경)
## [3.웹서비스](#웹서비스)
## [4.사용스타일](#사용스타일)
## [5.HTML](#HTML)
## [6.CSS](#CSS)
## [7.JS](#JS)
## [8.동적파라미터](#동적_파라미터)
## [9.랜더링](#HTML로_응답하기->랜더링)
## [10.GET방식](#GET_방식)
## [11.POST 방식](#POST_방식)
## [12.RestAPI 기법이용](#RestAPI_기법을_이용)
## [13.코드 적용](#코드_적용)


<hr>

## __목적__
    - 무엇을 만들것인가? 무엇을 주고 받을 것인가?
    - 파이썬으로 웹프로그래밍 구현
    - 웹의 환경 이해
    - 클라이언트 사이드 요소 이해
        - HTML, CSS, JavaScript
    - 서버 사이드 구성 (Flask)
    - 데이터베이스 사용 및 SQL처리 (maria)
        - RDBMS 계열중 mysql계열인 mariaDB
    - **데이터 수집관련 웹에 대한 백엔드 이해**
    - 파이널 프로젝트의 산출물의 형태로 사용가능
    - cms(adminLTE 스킨적용), ajax 
    - 웹소켓을 이용한 실시간 통신(채팅) 
<hr>

## __개발환경__
    - AWS 가입 미리 해둔다
    - github 가입 미리 해둔다.
    - python(or anaconda) + IDE(vs code)

### __파이썬 웹__
    - 마이크로 에디션 => nodejs
        - flask
            - $ pip install flask
        - 자유도가 높고, 딥러닝등 이식이 쉽다.
        - 주피터 노트북은 flask로 만들어졌다.
        
    - 풀 스펙 에디션 => Java : spring
        - Django
<hr></hr>
<br>

## __웹서비스__ 
<br/>

### _part1_
    - 클라이언트 사이드 : 프런트
        - 디자이너
        - html 코더 -> html5, css3
        - 자바 스크립트 개발자, 인터렉션, 통신 등등 개발 -> js
            CSS, JS에서는 selector(찾는다.), 이벤트 처리(통신, DOM조작, 인터렉션)
        or
        - Angular/Reactjs/Vue 개발자는 html, css, js를 한명이 다한다.
            - 프레임웍 <-> 서버 : 미들웨어 역할 <-> 데이터베이스
            - 커스텀 태그가 보이면 이방식으로 개발되었을 가능이크다.
### _part2_
    - 서버 사이드 : 백엔드

        * 플랫폼
            - 마이크로 에디션 -> 모든 것을 내가 다 하나부터 열까지 다 만든다. (자유도!!)
                - 최소의 룰만 가지고 자유롭게 구성
                - Node.js, flask(파이썬)
                - ex) flask의 대표작품 => 주피터 노트북
            
            - 풀스펙 에디션 -> 모든 것을 룰에 의해 짠다. (프레임웍 -> 규칙을 배워야한다.)
                - spring(java), Django(파이썬)

        * 개발 
            - URL 정의 (고급기능 -> 블루프린트를 사용, 업무별로 분할)
                - 기획서상의 세부페이지, 스토리보드, 프로토콜표
            - 화면을 중시 -> 웹서비스
            - 화면이 없다 -> 미들웨어 서버, API서버, 디비와의 쿼리가 중요
### _part3_
    - 데이터 베이스
        - RDBS
            - 엔터급
                - Oracle, ms-sql, 기업용, 오로라(AWS)
            - 일반 유저급
                - my-sql, maria, ...
                - maria를 이용 필요한 SQL은 그때 그때 사용
        
        - NoSQL
            - 몽고db
            - 클라우드 기반 (aws(아마존), azure(MS) 등등..)
            - firebase(구글)에서 실시간 DB도 지원            


<hr></hr>
<br>

## __사용 스타일__
<br>

<pre>
- 1. 서버 개발
- 2. 서버 가동
- 3. 브라우저 가동 
- 4. 브라우저 주소 가입, 엔터 => 요청, requset
- 5. 요청은 TCP/IP기반 http 프로토콜로 인터넷망을 이동 주소를 찾아서 서버로 도착
- 6. 서버는 라우터에 의해서 해당 요청을 처리하는 함수를 찾는다.
- 7. 함수가 해당 요청을 받아서 비즈니스 로직을 처리한다 ( Controller )
- 8. 필요하면 데이터베이스에 가서 쿼리를 수행후 데이터를 가져온다.
- 9. 이렇게 데이터가 준비되면 비즈니스 로직에 의해 응답 데이터를 구성
    구성된 데이터가 html으면 (View)라고 하고, 응답한다 -> MVC 모델
- 10. 응답 데이터는 인터넷을 타고 클라이언트 브라우저에 도착
- 11. 브라우저는 이 데이터를 파싱 (DOM이 구성)한다.
    파싱은 html, xml, json 등등 마크업랭귀지, 데이터 포맷등을 분석해서 원하는 데이터를 추출하는 과정
- 12. 브라우저는 순서대로 랜더링하게 되고, 우리는 화면을 보게 된다.
</pre>
<hr></hr>
<br>

## __HTML__
    - HyperText Markup Language   
    - 쉽고, 간결하여 브라우저상에서 콘텐츠의 구조와 내용을 담당하여 표현
    - 골격, 구조, 콘텐츠 내용 자체
    - 마크업랭귀지인 HTML은 현재 HTML5를  따르고, 이에 대한 표식
        맨 위에 <!DOCTYPE HTML> 이다.
    - ML은 엘리먼트로 구성되어 있다.
        - 엘리먼트(element)는 
            - 시작태그 (start tag) : <h1>
                - 속성을 가질수 있다. : <a href = 'http://...'>, href가 속성
            - 콘텐츠 (contents, 자식) : 어떤 것이든 올 수 있다.
            - 닫기태그 (end tag) : </h1>

<hr></hr>
<br>

## __CSS__
    - 브라우저 상에 콘텐츠의 레이아웃, 디자인을 담당한다.
    - 구성 : select(찾아라) + 디자인요소 (디자인 + 미디어쿼리 + 애니메이션)
    - selector => 데이터 수집(웹을 대상으로)시 기본 기술
<hr></hr>
<br>
    
## __JS__
    - 브라우저 상에 콘텐츠의 이벤트, 통신, 화면 조정등 사용자와 컨텐츠 간에 인터렉션 (상호작용성)을 담당한다.
    - 구성 : css selector + 이벤트처리(화면조작, 이벤트, 통신 ... )
     
<hr></hr>
<br>

## 클라이언트 사이드에서 콘텐츠 화면
    - HTML + CSS + JS로 구성한다.
<hr></hr>

## 동적_파라미터
    - 클라이언트가 특정 페이지를 요청할때, 데이터를 서버로 보낼수 있다.
    - case1 : method를 이용하여 전송, GET, POST, PUT, DELETE ...
        * http 프로토콜을 이용하여 데이터를 전송
        * 메소드에 따라 목적과 방식, 스타일, 화면 반응이 다르다
        * GET, POST에 집중하여 작업
    - case2 : url에 싣어서 전송 -> 동적 파라미터 (크기제한은 있음)
<hr> </hr>

## HTML로_응답하기->랜더링
<br>
<pre>
- from flask import Flask, render_template
- template 폴더를 생성한다.
</pre>

~~~ python
@app.route('/show')
def home():
    # HTML을 수정한다고 해서 서버가 재가동되지 않는다.
    # html은 반드시 templates 폴더 이하에 파일로 저장한다.
    return render_template('index.html')
~~~
<hr> </hr>

## GET_방식
<br>
<pre>

- 요청주소의 형태 : URL?키=값 & 키=값 & ...
- uid, upw 추출 => 클라이언트가 보낸 데이터
- 전달된 데이터는 어디를 타고 들어오는가? => 요청객체
- get 방식으로 전달된 데이터 추출 
- 개별 요청별로 알아서 전달되닌깐, request를 객체로 바로 사용하면 된다.
</pre>

~~~ python
from flask import Flask,render_template, request

# args.get 사용
@app.route('/loginProc')
def loginProc():
    # get 형식으로 uid키에 대한 값을 가져옴
    uid = request.args.get('uid') 
    upw = request.args.get('upw')
    print(uid, upw)
    return 'loginProc 페이지'
~~~
<hr>

## POST_방식
<br>
<pre>

- 기본은 GET만 허용한 라우팅 => GET은 정보가 URL에 노출
- 로그인 정보는 POST방식으로 전송
    * 보안이 필요한 데이터, 파일(크기가 큰 데이터) 전송에 적합
</pre>

~~~ python
from flask import Flask,render_template, request, redirect

# form.get 사용
@app.route('/loginProc', methods=['POST'])
def loginProc():
    uid = request.form.get('uid') 
    upw = request.form.get('upw')
~~~
<hr>

## RestAPI_기법을_이용
<br>
<pre>

- URL을 남발하지 않고, 업무별로 한개의 URL에서 처리되게 구성
- methods =['GET', 'POST']
</pre>
~~~python
@app.route('/login', methods=['GET','POST']) 
def login():
    if request.method == 'GET': # 화면 처리 담당
        ...

    else: # POST
        ...
~~~

## 코드_적용
<br>

~~~ python
# f_1.py 기본 템플릿

# TODO step 1 : 모듈 가져오기
# 실행 : python f_1.py
from flask import Flask

# TODO step 2 : Flask 객체 생성
app = Flask( __name__ )

# TODO step 3 : URL을 정의
@app.route('/')
def home():
    return "hello Flask Home page"     

# TODO step 4 : 서버가동 -> 엔트리 포인트 지정, 시작점 설정
if __name__ == '__main__':
    app.run(debug=True)
~~~
<br>

~~~ python
# f_2.py URL 추가, 깊이추가하기

# TODO step 1 : 모듈 가져오기
from flask import Flask

# TODO step 2 : Flask 객체 생성
app = Flask( __name__ )

# TODO step 3 : URL을 정의
@app.route('/')
def home():
    return "hello Flask Home page"     

# URL 추가
@app.route('/login')
def login():
    return "로그인하세요"

# 깊이 추가가능
@app.route('/logout/out')
def logout():
    return "로그아웃하세요"

# TODO step 4 : 서버가동 -> 엔트리 포인트 지정, 시작점 설정
if __name__ == '__main__':
    app.run(debug=True)
~~~