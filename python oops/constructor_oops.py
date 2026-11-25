'''Constructor is a special method in a class that is called automatically when object 
is created'''

class Student:
    def __init__(self):
        print("ulala")

s1=Student()   #--> Here you can see without calling a object the output is given...


'''Parameterized constructor --> It accepts additional parameter along with self allows you to 
pass different values for each object during creation '''

'''class ClassName:

    def __init__(self,para1,para2):
        self.para1=para1
        self.para2=para2 '''


class Student:

    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)

s1=Student("Saloni",20) 

'''Non-parameterized constructor --> It does not accept additional parameter ,only accepts
self as an argument'''

'''class Classname:
        def __init__(self):
            statements'''

class Student:

    def __init__(self):
        self.name="Ayushi"
        self.age=15
        print(self.name,self.age)

s1=Student() 





