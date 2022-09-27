# function1.py
#리턴하지 않는 함수
def setValue(newValue):
    #지역변수
    x = newValue
    print("지역변수:", x)

#함수 호출(중단점 지정)
retValue = setValue(5)
print(retValue)

#함수 정의
def swap(x,y):
    return y,x 

#호출
print( swap(3,4) )

print("---불변형식---")
a = 1.2 
print( id(a) )
a = 2.3 
print( id(a) )

print("---가변형식---")
lst = [1,2,3]
print( id(lst) )
lst.append(4)
print( id(lst) )
