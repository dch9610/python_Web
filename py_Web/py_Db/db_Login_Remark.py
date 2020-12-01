import pymysql as my

# 1.DB 연결
# 1-1 DB 오픈
def db_selectLogin(uid,upw):   
    conn = None # 선언 및 초기화
    row = None # 정보가 일치하지 않았을 때 함수의 리턴값
    
    try:
        conn = my.connect(host='localhost',  # 127.0.0.1
                        user='root',
                        password='12341234',
                        port=3306,  # 포트가 다른경우만
                        db='python_db',
                        charset='utf8mb4',
                        # 출력값 형태를 Dict로 받게함
                        cursorclass=my.cursors.DictCursor)
        print("연결 성공")
        # -----------------------------------
        # sql 실행, select 계열
        # cursor()를 통해 만들어지는 커서 객체로 쿼리 수행

        # 결과 집합이 딕셔너리, [딕셔너리, 딕셔너리,.. ] 형태로 와야함
        # 1. 커서를 뽑을 때 dict로 처리하겠다 (커서타입지정)
        # with conn.cursor(my.cursors.DictCursor) as cursor:
        # 2. 연결할때 dict로 받겠다.
        with conn.cursor() as cursor:
            # 1. sql문 준비
            # 파라미터 값을 받을수 있게 uid = %s AND upw=%s; 설정
            sql = '''
            SELECT
                *
            FROM 
                users
            WHERE
                uid = %s AND upw=%s;
            '''
            
            # 2.쿼리 수행
            cursor.execute(sql,(uid,upw))

            # 3.결과 집합 획득, 비동기적으로 일치되는 데이터 1개를 가져온다 
            # fetchone, 회원 로그인인므로 (회원은 고유하다, 유일하다)
            row = cursor.fetchone()

            # 4. 후처리
            # print(row)
            # 4-1 이름 출력
            # print(row[3])

            # 테이블 구조가 바뀌면 (컬럼순서변경) 이에 따라서 개발자는 
            # 수정을 해야한다. -> 구조가 변경되어도, 서비스가 영향을 안받게 하고 싶다
            # => 순서에 기반해서 처리했다 => 순서에 상관없이 처리하는 구조로 업데이트
            # => dict로 교체
            pass
        # -----------------------------------

    except Exception as E:
        print('예외발생', E)
        pass

    finally:
        # 2. DB 연결 해제
        if conn: # 변수가 False가 아닌 값을 가지고 있으면 참
            conn.close()
            # print("연결 해제")
    # 아이디 비번이 일치하면 > 데이터가 리턴
    # 아이디 비번 불일치 -> None
    return row

# 단위 테스트, 개별함수를 직접 테스트하기 위해서 삽입
if __name__ == '__main__':
    row = db_selectLogin('guest','1234')
print(row)
row = db_selectLogin('bu','1')
print(row)
print('-' * 10)
row = db_selectLogin('bu','1234')
print(row)