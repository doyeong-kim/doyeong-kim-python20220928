# demoStr.py
# print(dir(str))

strA = "python is very powerful"
strB = "파이썬은 강력해"
print(len(strA))
print(len(strB))
print(strA.capitalize())
print(strA.upper())
print(strA.count("p"))
print(strA.count("p", 7))

print("--반복 문구--")
names = ["홍길동", "전우치", "이순신"]
for name in names:
    print("안녕하세요 {0} 님 멋진 가을입니다.".format(name))
    print("=" * 40)

print("demo.ppt".startswith("demo"))
print("demo.ppt".endswith("ppt"))
print("MBC2580".isalnum())
print("MBC:2580".isalnum())
print("2580".isdecimal())

print("문자열 전처리---")
u = "<<< spam and ham >>>"
result = u.strip("<> ")
print(u)
print(result)
result = result.replace("spam", "spam-egg")
print(result)

print("---리스트---")
lst = result.split()
print(lst)
print("---다시 합치기---")
print( " ".join(lst) )