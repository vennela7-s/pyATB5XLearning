class Person:
    def __init__(self,name):
        self.name = name
    def walk(self):
        return self.name
person1 = Person("Venn")
person2 = Person("Usha")
print(person1.name)
print(person2.name)
print(person1.walk())
print(person2.walk())