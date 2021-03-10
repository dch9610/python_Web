from flask import Blueprint
from flask import render_template
from flask import session

from database import board_dao
from database import content_dao

# blueprint 객체 생성
main_blue = Blueprint('main', __name__)

# main을 요청하면 호출되는 함수
@main_blue.route('/main')
def main() :
    # 게시판 이름 정보를 가져온다.
    board_data = board_dao.selectBoardDataAll()
    # print(board_data)

    # 각 게시판별 상위 글 5개의 데이터를 담을 리스트
    content_list =[]

    for board_idx, board_name in board_data:
        # 게시판별 첫 페이지 게시글을 가져온다.
        a1 = content_dao.selectContentDataAll(board_idx, 1)
        # print(a1[:5])
        content_list.append(a1[:5])
    # print(content_list)

    # html 데이터를 랜더링한다.
    html = render_template('main/main.html', board_data = board_data,
                            content_list = content_list)

    return html