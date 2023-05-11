from typing import Any


class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Price: {self.price}"
    
    def __call__(self, title, author, price, pages):
        if pages > 400:
            raise ValueError("Not allowed to call and execute")
        
        else:
            self.title = title
            self.author = author
            self.price = price

b1 = Book("Grahsobha", "Aman", 100)

print(b1)

b1("Sarita", "Chikki", 300, 400)

print(b1)
        