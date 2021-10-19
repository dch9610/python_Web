# CSS

## 선택자의 역할
선택자는 HTML에 스타일(CSS)를 적용하기 위해 HTML의 특정한 요소를 선택하는 사인입니다.

<pre>
div{
    font-size : 20px;
    color : red;
}

선택자 {
    속성 : 값;
    속성 : 값;
}
</pre>

### 태그로 찾기
<pre>
h1 {
  color: red;
}

p {
  color: blue;
}
</pre>

### 클래스로 찾기
<pre>

.title {
  color: red;
}

.main-text {
  color: blue;
}
</pre>

--- 
## 속성과 값
속성과 값은 글자색은 무엇, 너비는 얼마, 여백은 얼마 같은 스타일을 지정할때 사용

<pre>
div {
    color : red; # 글자색은 빨강
    font-size : 20px; # 글자 크기는 20px
    width : 300px; # 가로 너비는 300px
    margin : 20px; # 바깥 여백은 20px
    padding : 10px 20px; # 안쪽 여백은 위아래 10px, 좌우 20px
    postiton : absolute; # 위치는 부모요소 기준
}
</pre>

---
## CSS 선언방식
### 태그에 직접 작성하기 (인라인)

<pre>
<div style = 'color : red'>태그에 직접 작성 </div> # style을 사용하여 직접 지정 
</pre>

### HTML에 포함하기 (내장)

<pre>
    head
        style
            div{
                color:red;
            }
        /style
    /head
</pre>

### HTML 외부에서 불러오기
분리된 하나의 CSS 파일을 여러 HTML 파일이 불러와서 사용
<pre>
 head
    (link rel = "stylesheet" href = "css 경로")
 /head
</pre>

---
## 속성
크기, 여백, 색상 같은 눈에 보이는 스타일을 지정

### 크기
- width(가로 너비) : 
요소의 가로 너비를 지정, 단위는 px(pixels)을 사용
- height (세로 너비) : 요소의 세로 너비를 지정합니다.
- font-size (글자 크기) :
요소 내용 (Text)의 글자 크기를 지정합니다.
<pre>
div {
    width : 200px;
    height : 200px;
    font-size :20px;
}
</pre>

### 여백
- margin(요소의 바깥 여백) : 
바깥 여백은 요소와 요소 사이의 여백(거리, 공간)을 생성할 때 사용
- padding(요소의 내부 여백) : 
요소의 내부 여백을 지정합니다. 내부 여백은 자식 요소를 감싸는 여백을 의미합니다.

<pre>
div{
    margin : 20px; # 요소바깥여백 
    margin-top : 20px; # 요소바깥여백-위쪽
    margin-right : 20px; # 요소바깥여백-오른쪽
    margin-bottom : 20px; # 요소바깥여백-아래쪽
    margin-left : 20px; # 요소바깥여백-왼쪽

    padding : 20px; # 요소내부여백
    padding-top : 20px; # 요소내부여백-위쪽
    padding-right : 20px; # 요소내부여백-오른쪽
    padding-bottom : 20px; # 요소내부여백-아래쪽
    padding-left : 20px; # 요소내부여백-왼쪽

}
</pre>

### 색상
- color(글자 색상) : 요소 내용의 글자 색상을 지정합니다.
- background(요소 색상) : 요소의 배경 색상을 지정

<pre>
div {
  color: red;
  background-color: red;
}
</pre>
