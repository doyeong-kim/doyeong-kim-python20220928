# demoFile.py
for x in range(1,6):
    print(x,"*", x , "=", x*x)

print("---서식지정=----")

for x in range(1,6):
    print(x,"*", x , "=", str(x*x).rjust(3))

print("---서식지정=----")

for x in range(1,6):
    print(x,"*", x , "=", str(x*x).zfill(3))


#서식지정
print("{0:x}", format(10)) #16진수로
print("{0:b}", format(10)) #이진수로
print("{0:e}", format(4/3))
print("{0:f}", format(4/3))
print("{0:.2f}", format(4/3))
print("{0:,}", format(15000000)) # 3자리마다 끊ㅇ어줘

#파일쓰기(raw string notation)
f = open(r"c:\work\demo.txt", "wt", encoding="utf-8")
#f = open("c:\\work\\demo.txt", "wt", encoding="utf-8")
f.write("첫번째\n두번째\n세번째\n")
f.close()

#파일 읽기
f = open("c:/work/demo.txt","rt", encoding="utf-8")
#처음부터 끝까지 하나의 문자열
result = f.read()
print(result)
#어디쯤 읽고 있어 ? 
print(f.tell())
#리셋해
f.seek(0)
lst = f.readlines()
#print(lst)
for item in lst:
    print(item, end="")

print("--한줄씩 처리--")
f.seek(0)
print(f.readline(), end="")
print(f.readline(), end="")

f.close()
