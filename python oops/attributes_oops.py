#Static Attribute --> Belongs to the class(class attribute)


class Student:
    name="aditya" #--> static attributes
    age=21

    def __init__(self):
        pass

print(Student.name) 
print(Student.age) 

s1=Student()
print(s1.name)
print(s1.age)



#Creating a new static attribute using classname

Student.gender="Male"
print(Student.__dict__)
print(s1.gender)

#To modify the existing static attribute we use classname

Student.name="pradeep"
print(Student.name)

#To delete a static attribute we use del keyword

del Student.age
print(Student.__dict__)
# print(Student.age) #--> attribute error 


#Non Static Attribute --> Belongs to a particular object(object/instance attribute)

class College:

    college_name="KLE"
    location="kamothe"

    def __init__(self,name,age):
        self.name=name
        self.age=age

s1=College('Chotta bheem',12) 
s2=College('Kalia',15)  
print(s1.__dict__)
print(s2.__dict__)     

#To access a nonstatic attribute we use object name

print(s1.name,s1.age)

#To add a nonstatic attribute we use object name

s1.gf="indumati"
print(s1.__dict__)

#To modify a nonstatic attribute we use object name

s1.gf="chutkii"
print(s1.__dict__)

#To delete a nonstatic attribute we use del keyword

del s1.gf
print(s1.__dict__)









