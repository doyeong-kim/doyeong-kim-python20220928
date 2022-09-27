# function2.py
#전역변수
x = 5 
def func(a):
    return a+x 

#호출
print( func(1) )

#지역변수
def func2(a):
    x = 1 
    return a+x 

#호출
print( func2(1) )

#디버깅 연습
def intersect(prelist, postlist):
    #지역변수에 리스트 초기화
    result = []
    #H(0) | A(1) | M(2)
    for x in prelist:
        #어떤 글자가 postlist에 있고 아직 result에 없으면(~이고, ~이면서) 
        if x in postlist and x not in result:
            result.append(x)
    return result

#호출
print( intersect("HAM","SPAM") )