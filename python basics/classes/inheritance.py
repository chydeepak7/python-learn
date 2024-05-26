class Person:
    def __init__(self, name , age):
        self.name = name
        # self.age = age
    def greet(self):
        return f'hi my name is {self.name}'

class Test(Person):
    def __init__(self,name,age):
        self.name = name
        self.age = age
ok = Test('deepak','2')
print(ok.greet())
