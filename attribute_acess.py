from typing import Any


class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        self.discount = 0.1
        self.freeGoodiesCount =1

    def __str__(self):
        titleString = self.title
        authorString = self.author
        cost = self.price
        goodCount = self.freeGoodiesCount
        formattedString = f"Title: {titleString}, Author: {authorString}, cost {cost}, Goodies{goodCount}"
        return formattedString
    
    def __getattribute__(self, name):
        if name == "price":
            p = super().__getattribute__("price")
            d = super().__getattribute__("discount")
            return p-(p*d)
        
        if name == "freeGoodiesCount":
            goodiesCount = super().__getattribute__("freeGoodiesCount")
            return goodiesCount+1
        
        return super().__getattribute__(name)
    
    def __setattr__(self, name, value):
        if name == "price":
            if type(value) is not float:
                raise ValueError("Trying setting value which is not float")
        return super().__setattr__(name, value)
    
    def __getattr__(self, name):
        return name + " is not here!"

b1 = Book("War", "jk rowling", 100.0)

print(b1)
print()
#b1.price = 40
print(b1.xyz)