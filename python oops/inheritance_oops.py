#Inheritance --> Allows one class to acquire attributes and methods of another class

'''Syntax:
class Parent:
    statements

class Child(Parent):
    statements    '''

class Animal:
    def __init__(self,name):
        self.name=name

    def eat(self):
        print(f"{self.name} is eating")  

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def sound(self):
        print(f"{self.name} says bow bow")  

class Cat(Animal):
    def sound(self):
        print(f"{self.name} says meow meow")

d1=Dog("Sheru")
d1.eat()
d1.sleep()
d1.sound() 

c1=Cat("Mani")
c1.eat()
c1.sleep()
c1.sound()

#Constructor calling statement-->It used for calling a constructor from parent class to child class

'''Two ways: 1.Parent Class Name
            2.Super method   '''

#Ex using parent class name

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Student(Person):
    def __init__(self, name, age,roll_no,marks):
        Person.__init__(self,name,age)
        self.roll_no=roll_no
        self.marks=marks

s1=Student("Pradeep",20,101,85)
print(s1.__dict__)

#Ex using super method

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Student(Person):
    def __init__(self, name, age,roll_no,marks):
        super().__init__(name,age)
        self.roll_no=roll_no
        self.marks=marks

s1=Student("Pradeep",20,101,85)
print(s1.__dict__)









