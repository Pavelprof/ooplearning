# The four principles of object-oriented programming (OOP) are encapsulation, inheritance,
# polymorphism, and abstraction. Here's a brief description of each principle with Python examples.
#
# Encapsulation:
# Encapsulation refers to the bundling of data and methods into a single unit called a class. It allows data hiding and protects the data from external interference. The class provides access to the data through methods, which can control the manipulation and modification of the data.
# Example:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)

person = Person("John", 25)
person.display_info()

# In this example, the Person class encapsulates the attributes name and age along with the display_info method.
# The attributes are accessed and modified through the class methods, providing control and encapsulation of the data.
#
# Inheritance:
# Inheritance allows creating a new class (derived class) from an existing class (base class).
# The derived class inherits the attributes and methods of the base class, allowing code reuse and promoting
# the concept of hierarchy.
# Example:

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

animal = Animal("Generic Animal")
animal.speak()

dog = Dog("Tommy")
dog.speak()

# In this example, the Animal class serves as the base class, and the Dog class is derived from it.
# The Dog class inherits the name attribute and the speak method from the Animal class.
# By overriding the speak method in the Dog class, we achieve polymorphism.
#
# Polymorphism:
# Polymorphism allows objects of different classes to be treated as objects of a common base class.
# It enables different classes to implement the same methods with different behaviors.
# This principle helps in achieving code flexibility, reusability, and extensibility.
# Example:

class Geom:
    def get_pr(self):
        raise NotImplementedError('The child class should redefine the method get_pr')

class Rectangle(Geom):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_pr(self):
        return 2*(self.w + self.h)


class Square(Geom):
    def __init__(self, a):
        self.a = a

#    def get_pr(self):
#       return 4 * self.a

r1 = Rectangle(1, 2)
r2 = Rectangle(3, 4)
sq1 = Square(10)
sq2 = Square(20)

geom = [r1, r2, sq1, sq2]

for g in geom:
    print(g.get_pr())

# Abstraction:
# Abstraction refers to the concept of hiding unnecessary implementation details and exposing only the essential features
# of an object. It allows creating abstract classes with abstract methods that act as a blueprint for the derived classes.
# Example:

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

# Abstract class cannot be instantiated
# animal = Animal()

dog = Dog()
dog.speak()

cat = Cat()
cat.speak()

# In this example, the Animal class is an abstract