# 데이터 베이스 생성
create database pusan_board_db
default character set utf8
collate utf8_unicode_ci;

# 데이터 베이스 사용설정
use pusan_board_db;

# 회원정보 테이블
# auto_increment : 자동으로 1씩 증가된값이 저장
create table user_table(
    user_idx int auto_increment not null,
    user_name char(10) not null,
    user_id varchar(100) not null,
    user_pw varchar(100) not null,
    constraint user_pk primary key(user_idx),
    constraint user_unique unique(user_id)
);

# 게시판 테이블
create table board_table(
    board_idx int auto_increment not null,
    board_name varchar(100) not null,
    constraint board_pk primary key(board_idx),
    constraint board_unique unique(board_name)
);

# 게시글 테이블
create table content_table(
    content_idx int auto_increment,
    content_subject varchar(500) not null,
    content_date date not null,
    content_writer_idx int not null,
    content_text varchar(500) not null,
    content_file varchar(500),
    content_board_idx int not null,
    constraint content_pk primary key(content_idx),
    constraint content_fk1 foreign key(content_writer_idx)
    references user_table(user_idx),
    constraint content_fk2 foreign key(content_board_idx)
    references board_table(board_idx)
);


# 테이블 삭제
# drop table user_table, user_board;

# 테이블 조인
select * from content_table a1, user_table a2
where a1.content_writer_idx = a2.user_idx;

# 해당 조건에 맞는 값들을 가져옴 (하나만 출력)
SELECT a2.user_name, a1.content_date, a1.content_subject,
		a1.content_text, a1.content_file, a1.content_writer_idx
 from content_table a1, user_table a2
where a1.content_writer_idx = a2.user_idx
	AND a1.content_idx =1 ;


# 해당 조건에 맞는 값들을 가져옴 (모든글 리스트)
SELECT a1.content_idx, a1.content_subject, a2.user_name,
		a1.content_date
 from content_table a1, user_table a2
where a1.content_writer_idx = a2.user_idx
	AND a1.content_idx =1 
order by a1.content_idx desc;