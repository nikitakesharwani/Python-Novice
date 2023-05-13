from dataclasses import dataclass

@dataclass
class Book:
    title : str
    author : str
    pages : int
    price : float

    def __post_init__(self):
        self.description = f"{self.title} by {self.author}, {self.pages} pages , Cost {self.price}"

b1 = Book("War & Peace" , "Jackey Morris" , 456 , 34.50)
b2 = Book("Half Blood" , "Nina Cox" , 877 , 89.90)

print(b1.description)
print(b2.description)
