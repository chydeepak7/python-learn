a = [1,2,3]
b = [4,5,6]
for x in zip(a,b):
    print(x)
for x in zip(a,b):
    print(*x)
for x,y in zip(a,b):
    print(x,y)
