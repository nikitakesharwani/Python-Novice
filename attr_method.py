class Vehicle:

    def __init__(self, category, weight, color):
        self.category = category
        self.weight = weight
        self.color = color
        

    def setPrice(self, price1):
        self.price = price1
    
    def setDiscount(self, amount1):
        self._DiscountAmount = amount1
    
    def getPrice(self):
        if hasattr(self, "_DiscountAmount"):
            print(self.price - (self.price * self._DiscountAmount))
        else:
            print(self.price)


truck1 = Vehicle("Truck", 1000 , "red") 

print(truck1.category)
truck1.setPrice(5000)
if hasattr(truck1, "price"):
    print(truck1.price)
else:
    print("not defined")
        
truck1.setDiscount(0.25)        
truck1.getPrice()