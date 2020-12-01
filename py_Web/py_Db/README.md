# 파이썬에서 Database 연동하기
## 1. 해당 db제품을 지원하는 모듈 사용 
</br>

[pymysql](https://github.com/PyMySQL/PyMySQL)

## 2. 패키지

  - [pymysql](https://github.com/PyMySQL/PyMySQL)
- 아나콘다
    - (가상환경명) $ conda install pymysql -y 무조건 yes
- 파이썬
    - $ pip install pymysql 


## 설정
- 예외처리문 사용
  - try ~ except ~finally

- 1. DB연결
~~~python
conn = my.connect(host='localhost',  # 127.0.0.1
                      user='root',
                      password='12341214',
                      port=3306,  # 포트가 다른경우만
                      db='python_db',
                      charset='utf8mb4',
                        # 출력값 형태를 Dict로 받게함
                    cursorclass=my.cursors.DictCursor)
~~~

- 2. 쿼리수행
~~~python
with conn.cursor() as cursor:
        # 1. sql문 준비
        sql = '''
        SELECT
            *
        FROM 
            users
        WHERE
            uid = 'bu' AND upw='1';
        '''
        
        # 2.쿼리 수행
        cursor.execute(sql)

        # 3.결과 집합 획득, 비동기적으로 일치되는 데이터 1개를 가져온다 
        # fetchone, 회원 로그인인므로 (회원은 고유하다, 유일하다)
        row = cursor.fetchone()
~~~

- 3. 단위테스트 수행
~~~python
if __name__ == '__main__':
    # 단위 테스트, 개별함수를 직접 테스트하기 위해서 삽입
    row = db_selectLogin('guest','1234')
    print(row)
    row = db_selectLogin('bu','1')
    print(row)
    print('-' * 10)
    row = db_selectLogin('bu','1234')
    print(row)
~~~