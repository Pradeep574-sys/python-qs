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
print(Student.age) #--> attribute error 


#Non Static Attribute --> Belongs to a particular object(class attribute)





