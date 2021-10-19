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