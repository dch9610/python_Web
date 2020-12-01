# TODO step 1: 모듈 가져오기

from flask import Flask,render_template,redirect,url_for,request
from py_Db.db_Login import db_selectLogin

# TODO step 2: Flask 객체 생성
app = Flask(__name__)

# TODO step 3: URL을 정의

@app.route('/')
def home():
    return 'Hi Flask'

# RestAPI 기법 적용
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    
    else: # POST
        uid =request.form.get('uid')
        upw =request.form.get('upw')
        user =db_selectLogin(uid,upw)
        print(user)
        
        # 유저 정보가 일치하면 함수 home으로 이동
        if user:
            return redirect(url_for('home'))

        else:
            msg1 = "[1] 회원이 아닙니다"
            return render_template('alter.html', msg = msg1)


# TODO step 4: 서버가동 -> 엔트리 포인트 지정, 시작점 설정
if __name__ == '__main__':
    app.run(debug=True)