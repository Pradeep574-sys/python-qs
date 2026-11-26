'''Encapsulation -->Process of binding data(variables) and methods inside a class
for data hiding and security'''

'''Access modifiers --> Controls the accessibility of class members,
important data from unauthorized access '''

#Public access modifier(default)

# class Product:

#     def __init__(self,id,name,price):
#         self.id=id
#         self.name=name
#         self.price=price

# p1=Product(101,'biscuit',20)
# print(p1.id)
# print(p1.name)
# print(p1.price)

# p1.price=50
# print(p1.price) #--> We access the price attribute and can modify its value which is not secure

#Protected access modifier(_)

class Product:

    def __init__(self,id,name,price):
        self.id=id
        self.name=name
        self._price=price

p1=Product(101,'biscuit',20)
print(p1.id)
print(p1.name)
print(p1._price)

p1._price=50
print(p1._price) # --> Python does not have strict protected access modifier






