import math
## Write your function here
def findGCD(a, b):
  x = (a+1)//2
  y = 1
  for i in range(1,x+1):
    if a%i==0 and 0 == b%i:
      y = i
  return y# return the gcd of numbers
print(findGCD(98,56))

# OR use this method
a = 98
b=56
print(math.gcd(a,b))