# a simple python class
class Person:
    # Constructor (initializer method)
    # sets attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to greet
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating an instance of the Person class
some_person = Person("Alice", 30)

# Accessing attributes and calling methods
print(some_person.name)
print(some_person.age)
some_person.greet()

