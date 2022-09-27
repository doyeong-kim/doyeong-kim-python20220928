# demoDict.py 
#딕셔너리 초기화
device = {"아이폰":5, "아이패드":10, "윈도우타블렛":20}
#입력
device["맥북"] = 30 
#수정
device["아이폰"] = 6 
for item in device.items():
    print(item)
#삭제
del device["아이폰"] 

for k,v in device.items():
    print(k, v)

#참조 복사
device2 = device 

device2["윈도우"] = 5 

print("참조를 전달")
print(device)
print(device2)
#id값을 출력
print( id(device) )
print( id(device2) )

print("---연산자---")
x = 10 
y = 20 
print(x == y)
print(x != y)
print(x <= y)
print(5/2)
print(5//2)
print(5%2)