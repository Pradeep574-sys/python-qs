#Class

''' class ClassName:
        attributes --> properties of object
        methods -->    functions written inside class '''

#Example

class Student:
    pass

s1=Student()
print(s1)
print(s1.__dict__)

class Student:
    a=10 #-->Attribute

    def __init(self): #--> Constructor
        pass

    def demo(self): #--> Instance Method
        pass

    @classmethod
    def demo2(cls): #--> Class Method
        pass

    @staticmethod
    def demo3(): #--> Static Method 
        pass 

    






