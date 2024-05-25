s = 'abc'
# result aaabbbccc
s = [x for x in s]
s = list(zip(s,s,s))
s = [''.join(y) for y in s]
s = ''.join(s)
print(s)
