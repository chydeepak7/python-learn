def issorted(a):
    min = a[0]
    for i in a:
        if min <= i:
            min = i
        else:
            return False
    return True
print(issorted([1,5,3,2]))