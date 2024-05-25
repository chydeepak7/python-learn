print({x for x in range(1, 10)}) # Set Comprehension
# strip() removes spaces in front or after the end of the string
# split() splits the sentence by spaces
test = '          deepak is done           '
print(test.strip())
print(test.split())
test = test.strip()
print(test)
dict_compre = {x+1:y for x,y in enumerate(test.split())}
print(dict_compre)
print(''.join(test.split()))
print(' '.join(test.split()))