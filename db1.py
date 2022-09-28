# db1.py
import sqlite3
#연결객체(일단은 메모리에서 작업)
con = sqlite3.connect(":memory:")

#구문을 실행하는 커서
cur = con.cursor()
#데이터 구조(table)
cur.execute("create table PhoneBook(Name text, PhoneNum text);")
#1건 입력
cur.execute("insert into PhoneBook values ('derick' , '010-111')")

#입력 파라메터 처리
name = "gildong"
phoneNumber = "010-222"
cur.execute("insert into PhoneBook values (?,?);" , (name,phoneNumber))

#여러 건 입력
datalist = (("tom","010-123"), ("dsp","010-5678"))
cur.executemany("insert into PhoneBook values (?,?);" , datalist)

cur.execute("select * from PhoneBook; ")
# for row in cur:
#     print(row)


print("-----fetchone()----")
print(cur.fetchone())
print("-----fetchmany(2)----")
print(cur.fetchmany(2))
print("----fetchall()0-----")
print(cur.fetchall())

