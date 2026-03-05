# 1️⃣ Single Inheritance
## One child class inherits from one parent class.
"""
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()   # Inherited method
d.bark()
"""


# 2️⃣ Multiple Inheritance
## One child class inherits from multiple parent classes.
"""
class Father:
    def skill1(self):
        print("Gardening")

class Mother:
    def skill2(self):
        print("Cooking")

class Child(Father, Mother):
    pass

c = Child()
c.skill1()
c.skill2()
"""


# 3️⃣ Multilevel Inheritance
## A class inherits from a class that already inherits from another class.
"""
class Grandparent:
    def home(self):
        print("Grandparent's home")

class Parent(Grandparent):
    pass

class Child(Parent):
    pass

c = Child()
c.home()
"""


# 4️⃣ Hierarchical Inheritance
## Multiple child classes inherit from one parent class.
"""
class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    pass

class Cat(Animal):
    pass

d = Dog()
c = Cat()

d.eat()
c.eat()
"""


# 5️⃣ Hybrid Inheritance
## Combination of two or more types of inheritance.
"""
class A:
    def methodA(self):
        print("A")

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

d = D()
d.methodA()
"""


# ✅ Summary
# | Type         | Meaning                      |
# | ------------ | ---------------------------- |
# | Single       | One parent → One child       |
# | Multiple     | Many parents → One child     |
# | Multilevel   | Grandparent → Parent → Child |
# | Hierarchical | One parent → Many children   |
# | Hybrid       | Mix of multiple types        |
