# 1️⃣ Basic class and object
class Person:
    pass

p1 = Person()
print("1️⃣ Created object of class:", p1)

# 2️⃣ Class with constructor (__init__) and attributes
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Sishir", 20)
print("2️⃣ Name:", s1.name, "Age:", s1.age)

# 3️⃣ Method inside class
class Greet:
    def say_hello(self):
        print("3️⃣ Hello from class!")

g = Greet()
g.say_hello()

# 4️⃣ Constructor + method
class Car:
    def __init__(self, brand):
        self.brand = brand
    
    def drive(self):
        print(f"4️⃣ Driving a {self.brand} car")

c = Car("Toyota")
c.drive()

# 5️⃣ Modify object properties
c.brand = "BMW"
print("5️⃣ Updated brand:", c.brand)

# 6️⃣ Add method to change value
class Product:
    def __init__(self, price):
        self.price = price

    def set_price(self, new_price):
        self.price = new_price

item = Product(50)
item.set_price(99)
print("6️⃣ New Price:", item.price)

# 7️⃣ Using default values
class Animal:
    def __init__(self, type="Dog"):
        self.type = type

a = Animal()
print("7️⃣ Animal type:", a.type)

# 8️⃣ Class with multiple attributes and a display method
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print(f"8️⃣ '{self.title}' by {self.author}")

b = Book("Python 101", "Siam")
b.display()

# 9️⃣ Class with list as attribute
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, name):
        self.books.append(name)

lib = Library()
lib.add_book("DSA Book")
print("9️⃣ Library books:", lib.books)

# 🔟 Private variable with __ (name mangling)
class Secret:
    def __init__(self):
        self.__code = "Hidden123"

    def reveal(self):
        print("🔟 Secret:", self.__code)

sec = Secret()
sec.reveal()

# 1️⃣1️⃣ Class with __str__ method (string representation)
class Player:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Player: {self.name}"

p = Player("Sishir")
print("1️⃣1️⃣", str(p))

# 1️⃣2️⃣ Class with class variable (shared across instances)
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

c1 = Counter()
c2 = Counter()
print("1️⃣2️⃣ Total objects created:", Counter.count)

# 1️⃣3️⃣ Inheritance (child class inherits parent)
class Parent:
    def speak(self):
        print("1️⃣3️⃣ I am parent")

class Child(Parent):
    pass

c = Child()
c.speak()

# 1️⃣4️⃣ Overriding method in child class
class Bird:
    def sound(self):
        print("Tweet")

class Duck(Bird):
    def sound(self):
        print("1️⃣4️⃣ Quack")

d = Duck()
d.sound()

# 1️⃣5️⃣ super() to call parent method
class Device:
    def info(self):
        print("Device Info")

class Phone(Device):
    def info(self):
        super().info()
        print("1️⃣5️⃣ Phone Info")

p = Phone()
p.info()

# 1️⃣6️⃣ Static method (doesn't need self)
class Math:
    @staticmethod
    def add(x, y):
        return x + y

print("1️⃣6️⃣ Static Add:", Math.add(5, 7))

# 1️⃣7️⃣ Class method (uses cls)
class Factory:
    version = 1

    @classmethod
    def get_version(cls):
        return cls.version

print("1️⃣7️⃣ Factory version:", Factory.get_version())

# 1️⃣8️⃣ isinstance() to check object type
print("1️⃣8️⃣ Is s1 a Student?", isinstance(s1, Student))

# 1️⃣9️⃣ Object inside object
class Engine:
    def __init__(self, power):
        self.power = power

class Vehicle:
    def __init__(self, engine):
        self.engine = engine

e = Engine("200HP")
v = Vehicle(e)
print("1️⃣9️⃣ Engine Power:", v.engine.power)

# 2️⃣0️⃣ List of objects
class User:
    def __init__(self, username):
        self.username = username

users = [User("Sishir"), User("Siam"), User("Raj")]
print("2️⃣0️⃣ Usernames:")
for u in users:
    print(u.username)