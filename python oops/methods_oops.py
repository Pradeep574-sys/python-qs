#Methods are the functions written inside a class


#Instance Method --> Belonging to a particular object

"""class Classname:
    def method_name(self,parameter):
        //statements """


class Car:
    company="TATA"

    def __init__(self,name,type): #init is a constructor that is automatically called when object is created
        self.name=name
        self.type=type

    def  display(self):
        print("Company: ",Car.company)
        print("Name:",self.name)
        print("Type:",self.type)

s1=Car('Nexon','Hatchback')
print(s1.__dict__)
s1.display()


#Another example

class College:
    college_name="Pillai"
    location="Panvel"
    pin_code=410208

    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course

    def biodata(self):
        print(f"Name:{self.name}\n Age:{self.age}\n Course:{self.course}")
        print(f"College Name:{College.college_name}\n Location:{College.location}\n Pin Code:{College.pin_code} ")

s1=College('Pradeep',21,'BCA')  
s2=College('Aditya',21,'BCA')  

s1.biodata()
s2.biodata()


#Class Method -->Method with @classmethod decorator and cls as a parameter 
'''class Classname:

    @classmethod
    def method_name(cls,parameter):
       //statements '''

class Student:
    college="Csmu"
    course="Python"

    @classmethod  #-->decorator
    def show(cls):
        print("College name: ",cls.college)
        print("Course: ",cls.course)

Student.show()
s1=Student()
s1.show()

#Static Method --> uses @staticmethod as a decorator does not require self or cls as its parameter

'''class Classname:

    @staticmethod
    def method_name(parameter):
       //statements '''

class  Student:

    @staticmethod
    def college_info():
        print("Hello Welcome")

Student.college_info()
s1=Student()
s1.college_info()






