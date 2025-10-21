import pymysql

# MySQL 서버에 연결
conn = pymysql.connect(
    host = "localhost", # host : MySQL주소 / "localhost" : 본인의 컴퓨터
    # port="3307",
    user = "root",
    password = "1234",
    database = "exampledb",
    charset = "utf8mb4", # utf-8의 확정버전
    cursorclass=pymysql.cursors.DictCursor
)

# 커서 생성(입력자) => 명령어 작성 가능하게 만듬
cursor = conn.cursor()

# 명령어 실행부분
sql1 = """
insert into employees(id, name, deptid, Managerid)
values(8,'kenneth',8,'101');
"""
cursor.execute(sql1)
conn.commit()

print("데이터 삽입 완료")

# cursor.execute("SELECT DATABASE()")
# cursor.fetchone() : 한번 호출에 하나의 Row를 가져올때 사용
# print(f"현재 데이터 베이스 : {cursor.fetchone()}") 
# print(f"현재 데이터 베이스 : {type(cursor.fetchone())}") # <class 'dict'>
# print(type(cursor.fetchone())) # <class 'NoneType'>

# cursor.fetchall() : 한번 호출에 전부의 Row를 가져올때 사용
# print(f"현재 데이터 베이스 : {cursor.fetchall()}") 
# print(type(cursor.fetchall())) # <class 'list'>

# # cursor.fetchall() : 한번 호출에 여러개의 Row를 가져올때 사용
# print(f"현재 데이터 베이스 : {cursor.fetchmany(2)}") 
# 연결 해제
conn.close()
