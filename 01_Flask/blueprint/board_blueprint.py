from flask import Blueprint
from flask import render_template
from flask.globals import request
from flask import session

from database import board_dao
from database import content_dao

import os
import time

board_blue = Blueprint('board', __name__)

# 게시글 리스트
@board_blue.route('/board_main')
def board_main() :
    # 파라미터 데이터 추출
    board_idx = request.args.get('board_idx')
    # print(board_idx)

    # 게시판 정보를 가져온다.
    board_data = board_dao.selectBoardDataOne(board_idx)
    # print(f'----------- {board_data}')

     # 현재 게시판의 글 목록을 가져온다.
    content_list = content_dao.selectContentDataAll(board_idx)

    # 응답결과를 랜더링한다.
    html = render_template('board/board_main.html', board_data = board_data, content_list = content_list, board_idx= board_idx)

    return html
# -------------------------------------------------------------


# 게시글 보는 페이지
@board_blue.route('/board_read')
def board_read() :
    # 파라미터 데이터를 추출한다.
    content_idx = request.args.get('content_idx')
    board_idx = request.args.get('board_idx')

    # print(content_idx)
    # print(board_idx)

    # 현재 글 정보를 가져온다.
    content_data = content_dao.selectContentDataOne(content_idx)
    # print(content_data)


    # 응답결과를 랜더링한다.
    html = render_template('board/board_read.html', content_data = content_data, board_idx =board_idx)

    return html
# -------------------------------------------------------------


# 글 수정 페이지
@board_blue.route('/board_modify')
def board_modify() :

    # 응답 결과를 랜더링한다.
    html = render_template('board/board_modify.html')
    return html
# -------------------------------------------------------------


# 글 작성 페이지
@board_blue.route('/board_write')
def board_write() :
    # board_idx 파라미터 추출
    board_idx = request.args.get('board_idx')
    # print(board_idx)

    # 응답 결과를 랜더링한다.
    html = render_template('board/board_write.html', board_idx = board_idx)
    return html
# -------------------------------------------------------------

# 글 작성 처리
@board_blue.route('/board_write_pro', methods=['post'])
def board_write_pro():

    # 데이터를 추출한다.
    content_subject = request.form.get('content_subject')
    content_writer_idx = session.get('login_user_idx')
    content_text = request.form.get('content_text')
    content_board_idx = request.form.get('content_board_idx')

    # print(content_subject)
    # print(content_writer_idx)
    # print(content_text)
    # print(content_board_idx)

    # 파일 업로드 처리
    # 첨부한 파일이 있을경우
    if request.files.get('content_file').filename != '':
        # content_file로 넘어오는 파일 데이터를 추출한다.
        content_file = request.files.get('content_file')

        # 중복을 방지하기 위해 파일이름에 시간을 붙여준다.
        file_name = str(int(time.time())) + content_file.filename
        # print(file_name)

        # 경로를 포함한 파일이름을 생성한다.
        a1 = os.getcwd() + '/static/upload/' + file_name
        # print(a1)

        # 저장한다.
        content_file.save(a1)
    
    # 첨부를 하지 않았을 경우
    else:
        file_name = None

    # 데이터베이스에 저장한다.
    content_dao.insertContentData(content_subject, content_writer_idx, content_text, 
                                    file_name, content_board_idx)

    # 방금 작성한 글의 인덱스를 가져온다.
    now_content_idx = content_dao.getMaxContentIdx(content_board_idx)
    # print(now_content_idx)

    return f'''
        <script>
            alert('작성되었습니다.')
            location.href = 'board_read?content_idx={now_content_idx}&board_idx={content_board_idx}'
        </script>
    '''