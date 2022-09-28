# demoRE.py

import re

#print(dir(re))

result = re.search("[0~9]*th", "  35th")
#매칭 오브젝트
print(result)
print(result.group())

#블록 주석 : ctrl+/
# result = re.match("[0~9]*th", "35th")
# print(result)
# print(result.group())

