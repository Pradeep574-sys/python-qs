class Car:
    company_name="TATA"

    def __init__(self,name,type,seats,fuel_type):
        self.name=name
        self.type=type
        self.seats=seats
        self.fuel_type=fuel_type

    def display(self):
        print("Company: ",Car.company_name)
        print("Name: ",self.name)
        print("Type: ",self.type)
        print("Seats: ",self.seats)
        print("Fuel: ",self.fuel_type)

c1=Car("Nexon","SUV",5,"EV")  
print(c1.__dict__)  
c1.display()

