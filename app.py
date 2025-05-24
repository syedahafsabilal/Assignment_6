##1
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")
s = Student("Alice", 90)
s.display()
##2
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def show_count(cls):
        print("[2]Total objects created:", cls.count)

Counter()
Counter()
Counter.show_count()

#3
class Car:
    def __init__(self,brand):
        self.brand = brand
    def start(self):
        print(f"[3]{self.brand}car is starting...")

c = Car("Toyota")
print("[3]Brand:",c.brand)
c.start()

#4
class Bank:
    bank_name = "ABC Bank"
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
b1 = Bank()
b2 = Bank()
Bank.change_bank_name("XYZ Bank")
print("[4]b1 bank name:",b1.bank_name)
print("[4]b2 bank name:",b2.bank_name)

#5
class MathUtils:
    @staticmethod
    def add(a,b):
        return a + b
print("[5]Sum:",MathUtils.add(5,3))

#6
class Logger:
    def __init__(self):
        print("[6]Logger started")

    def __del__(self):
        print("[6]Logger started")

l = Logger()
del l

#7
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

e = Employee("John", 50000, "123-45-6789")
print("[7] Public:", e.name)
print("[7]Protected:", e._salary)
print("[7] Private (name mangling):", e._Employee__ssn)

#8
class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

teacher = Teacher("Hafsa","Math")
print("[8] Teacher:", teacher.name, teacher.subject)

#9
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h 
    def area(self):
        return self.w * self.h
r = Rectangle(4, 5)
print("[9] Area:", r.area())

#10
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"[10] {self.name} says woof!")

Dog("Rex", "Bulldog").bark()

#11
class Book:
    total_books = 0

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

Book.increment_book_count()
Book.increment_book_count()
print("[11] Total books :", Book.total_books)

#12
class TemperatureConverter:
    @staticmethod
    def c_to_f(c):
        return (c * 9/5) + 32

print("[12] Celsius to Fahrenheit:", TemperatureConverter.c_to_f(0))

#13
class Engine:
    def start(self):
        print("[13] Engine started")
class CarWithEngine:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()
car = CarWithEngine(Engine())
car.start()

#14
class EmployeeAgg:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, employee):
        self.employee = employee

emp = EmployeeAgg("Abdullah")
dept = Department(emp)
print("[14] Employee in Department:", dept.employee.name)

#15
class A:
    def show(self):
        print("[15] A")

class B:
    def show(self):
        print("[15] B")

class C:
    def show(self):
        print("[15]C")

class D(B, C):
    pass

D().show()

#16
def log_function_call(func):
    def wrapper():
        print("[16] Function is being called")
        func()
    return wrapper

@log_function_call
def say_hello():
    print("[16]Hello!")

say_hello()

#17
def add_greeting(cls):
    cls.greet = lambda self: "[17] Hello from Decorator!"
    return cls

@add_greeting
class PersonDecorated:
    pass

print(PersonDecorated().greet())

#18
class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        self._price = value
    @price.deleter
    def price(self):
        del self._price
p = Product(100)
print("[18] Price:", p.price)
p.price = 150
print("[18] Updated Price:", p.price)
del p.price

#19
class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    def __call__(self, x):
        return x * self.factor

m = Multiplier(3)
print("[19] Callable:", callable(m))
print("[19] Called:", m(10))

#20
class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 118:
        raise InvalidAgeError("[20] Age must be 18+")
try:
    check_age(16)
except InvalidAgeError as e:
    print("Error:", e)

#21
class Countdown:
    def __init__(self, start):
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        if self.current < 0:
           raise StopIteration
        val = self.current
        self.current -= 1
        return val
print("[21] Countdown:")
for i in Countdown (5):
    print(i)