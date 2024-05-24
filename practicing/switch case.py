# There is no default switch statement in python but there are alternatives
# we can use if-else and many other methods but the most efficient method is to use dictionary

a = {
    1: 'deepak',
    2:'test',
    3:'testing',
    4: 'haha'
}
b = int(input('enter a numerical choice'))
try:
    print(f"{a[b]}")
except:
    print('enter a valid number')