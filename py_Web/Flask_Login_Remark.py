# 파이썬을 이용하ㅕ 웹서비스를 개발하는 기술 습득
# 모델 (머신러닝 / 딥러닝 등으로 학습한 결과물)을 동일한 언어로 서비스하기 위해
# 파이썬으로 웹서비스 구성법을 익힌다.
# flask를 이용한 간단한 웹페이지 구성 및 구성요소 이해

# 0단계 필요 모듈 설치
'''
    # $ pip install flask
    # $ conda install flask
'''


# TODO step 1 : 모듈 가져오기
# 실행 : python f_1.py
from flask import Flask

# TODO step 2 : Flask 객체 생성
app = Flask( __name__ )

# TODO step 3 : URL을 정의하고, 
# 특정 URL을 요청시 처리하는(요청을 처리, 응답을 구성, 실제 응답 수행)
# 함수를 정의하여 매칭한다.
# 고유한 URL 1개와 함수 1개를 매칭한다. 
# -> 전제      : 웹서비스, 기획서 -> 스토리보드 존재가 필요 
# -> 프로토콜표 : 미들웨어 서비스, 화면이 없는 웹서비스
#                이런 경우 웹의 화면, 서비스는 전부 클라이언트가 담당한다.
#                ex) reactjs, angular, vue => js or 타입스크립트로 클라이언트 개발


# @ : 데코레이터 -> 자바에서는 어노테이션이라고 부름
# '/' : URL -> 서버상의 특정 페이지의 주소 => 홈페이지를 의미
# '/' => 홈페이지를 의미 ex) http://m.naver.com
@app.route('/')
def home():
    # 현재로써는 함수내부 문자열을 리턴해야 한다!! 이것만 유지
    return "hello Flask Home page"     

# TODO step 4 : 서버가동 -> 엔트리 포인트 지정, 시작점 설정
# 내가 부르면 작동
if __name__ == '__main__':
    # 상용모드, 소스를 수정해도 반영되지 않는다.
    app.debug = True
    app.run()

    

# 5000번은 flask의 시그니처 포트
# http://127.0.0.1:5000