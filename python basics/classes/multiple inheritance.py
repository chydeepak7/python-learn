class Names:
    def __init__(self,name):
        self.name = name
    def namea(self):
        return (f"the name is {self.name}")
class Age:
    def __init__(self,age):
        self.age = age
    def ages(self):
        return (f"the age is {self.age}")
class Person(Names,Age):
    def __init__(self,name,age):
        Names.__init__(self,name)
        Age.__init__(self,age)
        self.name = name
        self.age = age
deepak = Person('deepak', 22)
print(deepak.namea())
print(deepak.ages())
