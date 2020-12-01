import pymysql as my

# 1.DB 연결
# 1-1 DB 오픈
def db_selectLogin(uid,upw):
    conn = None
    row = None
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
        with conn.cursor() as cursor:
            # 1. sql문 준비
            sql = '''
            SELECT
                *
            FROM 
                users
            WHERE
                uid = %s AND upw = %s;
            '''

            cursor.execute(sql,(uid,upw))

            row = cursor.fetchone()

        
        # -----------------------------------

    except Exception as E:
        print('예외발생', E)
        pass

    finally:
        if conn:
            conn.close()

    return row

if __name__ == '__main__':
    # 단위 테스트, 개별함수를 직접 테스트하기 위해서 삽입
    row = db_selectLogin('guest','1234')
    print(row)
    row = db_selectLogin('bu','1')
    print(row)
    print('-' * 10)
    row = db_selectLogin('bu','1234')
    print(row)
