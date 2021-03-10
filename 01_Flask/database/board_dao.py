from database import connector

# 게시판 정보 저장
def insertBoardData(board_name) :
    # 쿼리문 작성
    sql = '''
            insert into board_table
            (board_name)
            values (%s)
          '''
    # 데이터베이스 접속
    conn = connector.get_connection()
    cursor = conn.cursor()
    # %s에 바인딩될 값을 설정
    data = (board_name)
    # 쿼리 실행
    cursor.execute(sql, data)
    conn.commit()
    # 데이터베이스 접속 종료
    conn.close()

# 게시판 데이터 전체를 가져오는 함수
def selectBoardDataAll() :
    # 쿼리문 작성
    sql = '''
            select * from board_table
            order by board_idx
          '''
    # 데이터베이스 접속
    conn = connector.get_connection()
    cursor = conn.cursor()
    # %s에 설정한 값
    # 쿼리문 실행
    cursor.execute(sql)
    result = cursor.fetchall()
    # 데이터베이스 접속 종료
    conn.close()

    return result

# 게시판 정보 하나를 가져오는 함수
def selectBoardDataOne(board_idx) :
    # 쿼리문 작성
    sql = '''
            select * from board_table
            where board_idx = %s
          '''
    # 데이터베이스 접속
    conn = connector.get_connection()
    cursor = conn.cursor()
    # %s에 들어갈 값 설정
    data = (board_idx)
    # 쿼리 실행
    cursor.execute(sql, data)
    result = cursor.fetchone()
    # 데이터 베이스 접속 종료
    conn.close()

    return result

# 게시판 정보를 수정하는 함수
def updateBoardData(board_name, board_idx) :
    # 쿼리문 작성
    sql = '''
            update board_table
            set board_name = %s
            where board_idx = %s
          '''
    # 데이터 베이스 접속
    conn = connector.get_connection()
    cursor = conn.cursor()
    # %s에 지정될 값 설정
    data = (board_name, board_idx)
    # 쿼리 실행
    cursor.execute(sql, data)
    conn.commit()
    # 데이터 베이스 접속 해제
    conn.close()

# 게시판 정보를 삭제하는 함수
def deleteBoardData(board_idx) :
    # 쿼리문 작성
    sql = '''
            delete from board_table
            where board_idx = %s
          '''
    # 데이터 베이스 접속
    conn = connector.get_connection()
    cursor = conn.cursor()
    # %s에 지정될 값 설정
    data = (board_idx)
    # 쿼리 실행
    cursor.execute(sql, data)
    conn.commit()
    # 데이터 베이스 접속 해제
    conn.close()


