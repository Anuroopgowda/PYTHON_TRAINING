class Person:
    "This is a person class"
    name='anuroop'
    age = 10
    def greet(self):
        print('Hello')
print(Person.age)
print(Person.greet)
print(Person.__str__)
harry = Person()
harry.greet()
