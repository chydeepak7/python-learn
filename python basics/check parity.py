# parity means to check if the number is odd or even
def checkparity(n):
    return True if n%2 == 0 else False
a = int(input("Enter a number: "))
print(checkparity(a))