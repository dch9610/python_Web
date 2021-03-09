import pymysql

# 데이터베이스 접속
def get_connection() :
    conn = pymysql.connect(host='127.0.0.1', user='root', password='12341234',
                           db='pusan_board_db', charset='utf8')

    return conn


