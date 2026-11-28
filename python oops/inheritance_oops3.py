# d)Hierarchical -->Multiple Child class inherits from single Parent class

'''Syntax:
class Parent:
    statements

class Child1(Parent):
    statements
    
class Child2(Parent):
    statements        ''' 

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def person_details(self):
        print("Name:",self.name)
        print("Age:",self.age)

class Student(Person):
    def __init__(self, name, age,marks,roll_no):
        super().__init__(name, age)  
        self.marks=marks
        self.roll_no=roll_no

    def student_details(self):
        self.person_details()
        print("Marks:",self.marks)
        print("Roll no:",self.roll_no)

class Teacher(Person):
    def __init__(self,name,age,emp_id,salary):
        super().__init__(name,age)
        self.emp_id=emp_id
        self.salary=salary

    def teacher_details(self):
        self.person_details()
        print("Emp_Id:",self.emp_id)
        print("Salary:",self.salary)

s1=Student("Pradeep Barik",20,98,101)
t1=Teacher("Asmita Mam",30,1203,40000)

s1.student_details()
print()
t1.teacher_details()


#e)Hybrid-->It Combines two or more types of inheritance,such as single,multi,multiple,hierarchical

'''Syntax:
class Parent:
    statements

class Child1(Parent):
    statements
    
class Child2(Parent):
    statements       

class Child3(Child1,Child2):
    statements              
    
class Child4(Child3):
        statements    '''



class Person:
    def __init__(self, name):
        self.name = name

    def person_details(self):
        print("Name:", self.name)


# Hierarchical Inheritance
class Student(Person):
    def __init__(self, name, roll_no):
        Person.__init__(self, name)
        self.roll_no = roll_no

    def student_details(self):
        print("Roll No:", self.roll_no)


class Teacher(Person):
    def __init__(self, name, subject):
        Person.__init__(self, name)
        self.subject = subject

    def teacher_details(self):
        print("Subject:", self.subject)


# Multiple Inheritance
class TeachingAssistant(Student, Teacher):
    def __init__(self, name, roll_no, subject, department):
        Student.__init__(self, name, roll_no)
        Teacher.__init__(self, name, subject)
        self.department = department

    def assistant_details(self):
        print("Department:", self.department)


# Single Inheritance
class ResearchAssistant(TeachingAssistant):
    def __init__(self, name, roll_no, subject, department, research):
        TeachingAssistant.__init__(self, name, roll_no, subject, department)
        self.research = research

    def research_details(self):
        print("Research:", self.research)


obj1 = ResearchAssistant("Pradeep", 101, "Python", "Computer Science", "Artificial Intelligence")

obj1.person_details()
obj1.student_details()
obj1.teacher_details()
obj1.assistant_details()
obj1.research_details()

    

