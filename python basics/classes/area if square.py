class Rectangle:
    def __init__(self, x1, y1, x2, y2):  # class constructor
        self.x1 = x1  # class variable
        self.y1 = y1  # class variable
        self.x2 = x2  # class variable
        self.y2 = y2  # class variable

    def width(self):
        return self.x2 - self.x1

    def height(self):
        return self.y2 - self.y1

    def area(self):
        return self.width() * self.height()

class Square(Rectangle):
    def __init__(self, x1, y1, l):
        self.x1 = x1
        self.y1 = y1
        x2 = self.x1 + l
        y2 = self.y1 + l
        super().__init__(x1,y1,x2,y2)

test = Square(2,3,50)
print(test.area())