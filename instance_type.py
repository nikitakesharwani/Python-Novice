class Car:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Bike:
    def __init__(self, name, price):
        self.price = price
        self.name = name

car1=Car("Tata Punch" , 10)
car2=Car("xuv500", 15)
bike1=Bike("pulsar200ns" , 1.50 )
bike2=Bike("royalenfield" , 2.50)

print(type(car1))
print(type(car2))
print(isinstance(bike1, Bike))
print(isinstance(bike2, Car))