# demoRE.py

import re

#print(dir(re))

result = re.search("[0~9]*th", "35th")
#매칭 오브젝트
print(result)
print(result.group())

#블록 주석 : ctrl+/
# result = re.match("[0~9]*th", "35th")
# print(result)
# print(result.group())

result = re.search("apple", "this is apple")
print(result.group())

print("--년도찾기--")
print( bool(re.search("\d{4}", "올해는 2022년")))
result = re.search("\d{5}", "우리 동네는 52300")
print(result.group())
