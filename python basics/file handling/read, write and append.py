f = open('example.txt', 'a')
print(f.write('da'))
f.close()
with open('example.txt',"a") as f:
    f.write("testing\n")
# with open('example.txt','r') as f:
#     print(f.read())
with open("example.txt",'a') as f:
    f.write('hahaha')
# f = open("example.txt", 'r')
# print(f.read())
# f.close()
with open('example.txt', 'r') as f:
    for i in f:
        print(i.strip())
