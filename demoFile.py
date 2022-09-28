# demoFile.py
for x in range(1,6):
    print(x,"*", x , "=", x*x)

print("---서식지정=----")

for x in range(1,6):
    print(x,"*", x , "=", str(x*x).rjust(3))

print("---서식지정=----")

for x in range(1,6):
    print(x,"*", x , "=", str(x*x).zfill(3))
