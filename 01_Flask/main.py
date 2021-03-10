from flask import Flask
from flask import redirect

# blueprint
from blueprint.main_blueprint import main_blue
from blueprint.board_blueprint import board_blue
from blueprint.user_blueprint import user_blue



# 서버역할을 할 객체 생성
# template_folder : 랜더링할 html 문서가 있는 곳(기본 - templates)
app = Flask(__name__, template_folder='views', static_folder='static')

# 세션영역 사용을 위한 암호화 키를 설정한다.
app.secret_key = 'p9pwefijeprgqjgijregf'

# blueprint 등록
app.register_blueprint(main_blue)
app.register_blueprint(board_blue)
app.register_blueprint(user_blue)

# 주소만 입력하고 들어왔을 경우 호출될 부분
@app.route('/')
def index() :
    # 브라우저에게 main을 요청하라는 응답 결과를 전달한다.
    return redirect('main')

# 서버 가동
# port : 80, 요청할 때 포트번호를 생략하고 요청할 수 있다.
# debug=True : 코드를 수정하면 서버가 재 가동한다.
app.run(port=80, debug=True)