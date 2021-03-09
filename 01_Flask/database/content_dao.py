from database import connector

# 게시글 정보를 추가하는 함수
def insertContentData(content_subject, content_writer_idx,
                      content_text, content_file, content_board_idx) :
    # 쿼리문 작성
    sql = '''
            insert into content_table
            (content_subject, content_date, content_writer_idx, 
            content_text, content_file, content_board_idx)
            values
            (%s, sysdate(), %s, %s, %s, %s)
          '''
    # 데이터베이스 접속
    conn = connector.get_connection()
    cursor = conn.cursor()
    # %s에 지정될 값 설정
    data = (content_subject, content_writer_idx, content_text,
            content_file, content_board_idx)
    # 쿼리 실행
    cursor.execute(sql, data)
    conn.commit()
    # 데이터 베이스 접속 종료
    conn.close()
# ----------------------------------------------------------


# 모든 글 정보를 가져오는 함수
def selectContentDataAll(content_board_idx) :
    # 쿼리문 작성
    sql = '''
            SELECT a1.content_idx, a1.content_subject, a2.user_name,
		              a1.content_date
            from content_table a1, user_table a2
            where a1.content_writer_idx = a2.user_idx
	            AND a1.content_idx = %s
            order by a1.content_idx desc;
          '''
    # 데이터베이스 접속
    conn = connector.get_connection()
    cursor = conn.cursor()
    # %s에 지정될 값 설정
    data = (content_board_idx)

    # 쿼리 실행
    cursor.execute(sql, data)
    result = cursor.fetchall()
    # 데이터 베이스 접속 종료
    conn.close()

    return result
# ----------------------------------------------------------


# 글 하나만 가져오는 함수
def selectContentDataOne(content_idx) :
    # 쿼리문 작성
    sql = '''
            SELECT a2.user_name, a1.content_date, a1.content_subject,
	              	a1.content_text, a1.content_file, a1.content_writer_idx
            from content_table a1, user_table a2
            where a1.content_writer_idx = a2.user_idx
	              AND a1.content_idx = %s ;
          '''
    # 데이터 베이스 접속
    conn = connector.get_connection()
    cursor = conn.cursor()
    # %s에 지정될 값 설정
    data = (content_idx)
    # 쿼리 실행
    cursor.execute(sql, data)
    result = cursor.fetchone()
    # 데이터 베이스 접속 해제
    conn.close()

    return result
# ----------------------------------------------------------


# 게시글 정보를 수정하는 함수
def updateContentData(content_subject, content_writer_idx,
                      content_text, content_file, content_board_idx,
                      content_idx) : 
    # 쿼리문 작성
    sql = '''
            update content_table
            set content_subject = %s, content_writer_idx = %s,
                content_text = %s, content_file = %s, 
                content_board_idx = %s
            where content_idx = %s
          '''
    # 데이터베이스 접속
    conn = connector.get_connection()
    cursor = conn.cursor()
    # %s에 지정될 값 설정
    data = (content_subject, content_writer_idx, content_text,
            content_file, content_board_idx, content_idx)
    # 쿼리 실행
    cursor.execute(sql, data)
    conn.commit()
    # 데이터 베이스 접속 종료
    conn.close()
# ----------------------------------------------------------


# 글 하나를 삭제하는 함수
def deleteContentData(content_idx) :
    # 쿼리문 작성
    sql = '''
            delete from content_table
            where content_idx = %s
          '''
    # 데이터베이스 접속
    conn = connector.get_connection()
    cursor = conn.cursor()
    
    # %s에 지정될 값 설정
    data = (content_idx)

    # 쿼리문 실행
    cursor.execute(sql, data)
    conn.commit()
    
    # 데이터 베이스 접속 종료
    conn.close()

# 방금 작성한 글의 번호 (글번호가 제일 큰것)을 가져온다.
def getMaxContentIdx(content_board_idx):
  # 쿼리문
  sql = '''
    select max(content_idx)
    from content_table
    where content_board_idx = %s
  '''

  # 데이터베이스 접속
  conn = connector.get_connection()
  cursor = conn.cursor()

  # %s 값 설정
  data = (content_board_idx)

  # 쿼리문 실행
  cursor.execute(sql, data)
  result = cursor.fetchone()

  # 데이터베이스 접속해제
  conn.close()

  return result