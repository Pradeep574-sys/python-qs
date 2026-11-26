#Private access modifier(__)

class Product:

    def __init__(self,id,name,price):
        self.id=id
        self.name=name
        self.__price=price

p1=Product(101,'biscuit',20)
print(p1.id)
print(p1.name)
# print(p1.__price) --> It will thrown an Attributeerror 
print(p1.__dict__)

#Ways to access and modify private member

#1.Name mangling --> python changes name of attriute/method to _Classname__attributename

class Product:
    def __init__(self,id,name,price):
        self.id=id
        self.name=name
        self.__price=price

p1=Product(101,"chocolate",100)
print(p1.id)
print(p1.name)
print(p1.__dict__)
print(p1._Product__price) # accessing the private member

#Modifying a private attribute using name mangling

#syntax - obj_name._ClassName__attributename=new_value

p1._Product__price=50
print(p1.__dict__)

#2.i] gettermethod(accessor) --> Gives access to the value of private members

'''Rules-I.Method name starts with get & followed by attributename.
        II.Only has self as a parameter.
        III.Must return the value of the attribute. '''

class Product:
    def __init__(self,id,name,price):
        self.id=id
        self.name=name
        self.__price=price

    def get_price(self):
        return(self.__price)    

p1=Product(101,"chocolate",100)
print(p1.get_price())

#2.ii] settermethod(mutator) --> Updates the value of private members

'''Rules-I.Method name starts with set & followed by attributename.
        II.Only has one additional parameter other than self.
        III.It should validate the value before assigning it. '''

'''Syntax - def set_Attributename(self,parameter):
                self.__attributename=parameter '''

class Product:
    def __init__(self,id,name,price):
        self.id=id
        self.name=name
        self.__price=price

    def get_price(self): #--> getter method
        return(self.__price) 

    def set_price(self,new_price): #--> setter method
        if new_price>0:            #--> validation
            self.__price=new_price
        else:
            print("Invalid Entry")       

p1=Product(101,"chocolate",100)
print(p1.get_price())
print(p1.__dict__)
p1.set_price(110)
print(p1.__dict__)


#3.iii] property decorator --> Built-in decorator allows us to use method like normal attribute

'''Rules-I.The getter,setter and propertyname should all be the same.
        II.The getter must be define before the setter.
        III.The setter decorator takes self + one parameter. '''

class Product:
    def __init__(self,id,name,price):
        self.id=id
        self.name=name
        self.__price=price

    @property
    def price(self): #--> getter method
        return(self.__price) 

    @price.setter     #--> names are same for getter,setter and propertyname
    def price(self,new_price): #--> setter method
        if new_price>0:            #--> validation
            self.__price=new_price
        else:
            print("Invalid Entry")       

p1=Product(101,"chocolate",100)
print(p1.price) #--> accessing private member's value like a normal attribute
print(p1.__dict__)
p1.price=110    #--> modifying private member's value like a normal attribute
print(p1.__dict__)














