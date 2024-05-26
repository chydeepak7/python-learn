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
class Person(Age,Names):
    def __init__(self,name,age):
        Names.__init__(self,age)
        super().__init__(age)

deepak = Person('deepak', 22)
print(deepak.namea())
print(deepak.ages())
