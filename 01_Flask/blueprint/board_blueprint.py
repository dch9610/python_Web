from flask import Blueprint
from flask import render_template
from flask import request
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
    page = request.args.get('page')
    if page == None:
        page = '1'
    page=int(page)

    # 페이지 번호가 0이하면..
    if page < 1:
        page=1

    # 게시판 정보를 가져온다.
    board_data = board_dao.selectBoardDataOne(board_idx)
    # print(f'---------------- {board_data}')

    # 현재 게시판의 글 목록을 가져온다.
    content_list = content_dao.selectContentDataAll(board_idx, page)

    # 게시판 종류에 따라 글의 개수를 가져온다.
    contentCnt = content_dao.getContentCnt(board_idx)
    # print(contentCnt[0])

    # 글의 개수를 이용해 전체 페이지 수를 구한다.
    pageCnt = contentCnt[0] // 10
    if contentCnt[0] % 10 > 0:
        pageCnt = pageCnt + 1

    # 현재 페이지 번호가 전체 페이지 수보다 크면 전체 페이지 개수로 넣어준다.
    if page > pageCnt:
        page = pageCnt


    # 현재 페이지 번호를 이용하여 pagination 시작값을 구한다.
    start_page = ((page-1) // 10 * 10) + 1

    # 전체 페이지 수를 이용해 pagination 종료값을 구한다.
    end_page = start_page + 9
    if end_page > pageCnt:
        end_page = pageCnt

    # print(pageCnt)
    # print(end_page)
    # print(page)

    # 응답결과를 랜더링한다.
    html = render_template('board/board_main.html', board_data=board_data, 
                            content_list=content_list, board_idx=board_idx, 
                            start_page = start_page, end_page = end_page,
                            page_cnt = pageCnt, page=page)

    return html

# 게시글 보는 페이지
@board_blue.route('/board_read')
def board_read() :
    # 파라미터 데이터를 추출한다.
    content_idx = request.args.get('content_idx')
    board_idx = request.args.get('board_idx')
    page = request.args.get('page')

    # print(content_idx)
    # print(board_idx)

    # 현재 글 정보를 가져온다.
    content_data = content_dao.selectContentDataOne(content_idx)
    # print(content_data)

    # 응답결과를 랜더링한다.
    html = render_template('board/board_read.html', content_data=content_data, 
                            board_idx=board_idx, page= page, content_idx = content_idx)

    return html

# 글 수정 페이지
@board_blue.route('/board_modify')
def board_modify() :
    # 파라미터 데이터 추출
    content_idx = request.args.get('content_idx')
    board_idx = request.args.get('board_idx')
    page = request.args.get('page')

    # print(content_idx)
    # print(board_idx)
    # print(page)

    # 현재 글 정보를 가져온다.
    content_data = content_dao.selectContentDataOne(content_idx)
    print(content_data)
    
    # 응답 결과를 랜더링한다.
    html = render_template('board/board_modify.html', content_data=content_data,
                            content_idx=content_idx, board_idx=board_idx,
                            page=page)
    return html

# 글 작성 페이지
@board_blue.route('/board_write')
def board_write() :
    # 파라미터 추출
    board_idx = request.args.get('board_idx')
    # print(board_idx)

    # 응답 결과를 랜더링한다.
    html = render_template('board/board_write.html',board_idx=board_idx)
    return html

# 글 작성 처리
@board_blue.route('/board_write_pro', methods=['post'])
def board_write_pro() :

    # 데이터를 추출한다.
    content_subject = request.form.get('content_subject')
    content_writer_idx = session.get('login_user_idx')
    content_text = request.form.get('context_text')
    content_board_idx = request.form.get('content_board_idx')

    # print(content_subject)
    # print(content_writer_idx)
    # print(content_text)
    # print(content_board_idx)

    

    # 업로드 처리
    # 첨부한 파일이 있을 경우
    if request.files.get('content_file').filename != '' :
        # board_file로 넘어오는 파일 데이터를 추출한다.
        board_file = request.files.get('content_file')
        # 중복을 방지하기 위해 파일이름에 시간을 붙혀준다.
        file_name = str(int(time.time())) + board_file.filename
        # print(file_name)
        # 경로를 포함한 파일이름을 생성한다.
        a1 = os.getcwd() + '/static/upload/' + file_name
        # print(a1)
        # 저정한다.
        board_file.save(a1)
    # 첨부를 하지 않았을 경우
    else :
        file_name = None

    # 데이터 베이스에 저장한다.
    content_dao.insertContentData(content_subject, content_writer_idx,
                        content_text, file_name, content_board_idx)

    # 방금 작성한 글의 인덱스를 가져온다.
    now_content_idx = content_dao.getMaxContentIdx(content_board_idx)
    # print(now_content_idx)

    return f'''
            <script>
                alert('작성되었습니다')
                location.href = 'board_read?content_idx={now_content_idx}&board_idx={content_board_idx}'
            </script>
           '''

# 삭제 
@board_blue.route('/board_delete')
def board_delete():
    # 파라미터 데이터 추출
    content_idx = request.args.get('content_idx')
    board_idx = request.args.get('board_idx')
    page = request.args.get('page')

    # print(content_idx)
    # print(board_idx)
    # print(page)

    # 삭제한다.
    content_dao.deleteContentData(content_idx)

    return f'''
        <script>
            alert('삭제되었습니다')
            location.href = 'board_main?board_idx={board_idx}&page={page}'
        </script>
    '''

# 수정완료 누를 시 반응
@board_blue.route('/board_modify_pro', methods=['post'])
def board_modify_pro():

    # 데이터를 추출한다.
    content_subject = request.form.get('content_subject')
    content_text = request.form.get('content_text')
    content_idx = request.form.get('content_idx')
    board_idx = request.form.get('board_idx')
    page = request.form.get('page')

    # print(content_subject)
    # print(content_text)
    # print(content_idx)
    # print(board_idx)
    # print(page)

    # 업로드 처리
    # 첨부한 파일이 있을 경우
    if request.files.get('content_file').filename != '' :
        # board_file로 넘어오는 파일 데이터를 추출한다.
        board_file = request.files.get('content_file')
        # 중복을 방지하기 위해 파일이름에 시간을 붙혀준다.
        file_name = str(int(time.time())) + board_file.filename
        # print(file_name)
        # 경로를 포함한 파일이름을 생성한다.
        a1 = os.getcwd() + '/static/upload/' + file_name
        # print(a1)
        # 저정한다.
        board_file.save(a1)
    # 첨부를 하지 않았을 경우
    else :
        file_name = None
    # print(file_name)

    # 수정처리
    content_dao.updateContentData(content_subject, content_text, file_name,
                                    content_idx)

    return f'''
            <script>
                alert('수정되었습니다')
                location.href = 'board_read?content_idx={content_idx}'
                              + '&board_idx={board_idx}&page={page}'
            </script> 
            '''