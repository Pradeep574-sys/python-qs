#Types of Inheritance

# a)Single-level --> One child class inherits properties of one parent class

'''Syntax:
class Parent:
    statements
    
class Child(Parent):
    statements        ''' 

class Person:
    def __init__(self,name):
        self.name=name

    def display_name(self):
        print(self.name)  

class Student(Person):
    def __init__(self,name,branch):
        super().__init__(name)  
        self.branch=branch

    def display_branch(self):
        print(self.branch)

s1=Student("Saloni","CS") 
s1.display_name()
s1.display_branch()  

# b)Multi-level -->Child class becomes parent class for another child class

'''Syntax:
class GrandParent:
    statements
class Parent(GrandParent):
    statements
    
class Child(Parent):
    statements        ''' 

class Person:
    def __init__(self,name):
        self.name=name

    def display_name(self):
        print(self.name)    

class Employee(Person):
    def __init__(self, name,emp_id):
        super().__init__(name)
        self.emp_id=emp_id

    def display_id(self):
        print(self.emp_id)

class Manager(Employee):
    def __init__(self, name, emp_id,dept):
        super().__init__(name, emp_id)
        self.dept=dept

    def display_dept(self):
        print(self.dept)

m=Manager("Aditya",36,"CSE")
m.display_name()
m.display_id()
m.display_dept()
print(m.__dict__)                                

# c)Multiple -->One Child class inherits from two or more Parent class

'''Syntax:
class Parent1:
    statements
class Parent2:
    statements
    
class Child(Parent1,Parent2):
    statements        ''' 

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def person_details(self):
        print("Name: ",self.name)
        print("Age: ",self.age)    

class Employee:
    def __init__(self,emp_id,salary):
        self.emp_id=emp_id
        self.salary=salary

    def employee_details(self):
            print("Emp_id: ",self.emp_id)
            print("Salary: ",self.salary)   

class Manager(Person,Employee):
    def __init__(self,name,age,emp_id,salary,dept):
        Person.__init__(self,name,age)
        Employee.__init__(self,emp_id,salary)
        self.dept=dept

    def manager_details(self):
        self.person_details()
        self.employee_details()
        print("Department: ",self.dept)
        
m1=Manager("Sahil",23,1201,30000,"Marketing")
m1.manager_details()     






