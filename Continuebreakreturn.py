#1.Skip at 4 using continue
for i in range (1,11):
    if i==4:
        continue
    print(i)

#2.Stops at 8 using break
for i in range (1,11):
    if i==8:
        break
    print(i)

#Add 20 and 10 by using return and loops
def add (a,b):
     return a+b
result=add(10,20)
print(result)