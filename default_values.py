
from dataclasses import dataclass , field
import random

def generate_random_num():
    return float(random.randint(20,60))



@dataclass
class Book:
    title : str = "No Title"
    author : str = "No Author"
    pages : int = 0
    price : float = field(default_factory= generate_random_num)

b1 = Book("Harry Potter" , "JK Rowling" , 787)
b2 = Book("Rich Dad Poor Dad" , "Robert Kiyosky" , 378)
print(b1)
print(b2)