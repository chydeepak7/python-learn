class Rectangle:
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    def width(self):
        print(self.x2-self.x1)
    def height(self):
        print(self.y1-self.y2)
    def area(self):
        print((self.x2-self.x1)*(self.y1-self.y2))
    def perimeter(self):
        print(2*((self.y1-self.y2)+(self.x2-self.x1) ))
    def __str__(self):
        return str(self.x1)
test = Rectangle(2,7,8,4)
test.width()
test.height()
print(test)
