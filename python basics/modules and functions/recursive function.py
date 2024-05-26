a = int(input("Enter a number: "))
def factorial(n):
    if n !=0:
        print(n)
        factorial(n-1)
factorial(a)