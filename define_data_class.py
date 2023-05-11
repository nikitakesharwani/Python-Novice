# Creating a data class.

from dataclasses import dataclass

@dataclass
class Book:     
    title : str
    author :  str
    price : float

    def editDetails(self, update):
        self.title = update

b1 = Book("C++" , "Yashwant Kanetkar" , 360)
b2 = Book("Java" , "Josh" , 564)
b3 = Book("C++" , "Yashwant Kanetkar" , 360)
print(b1)
print(b1 == b3)
b1.editDetails("C")
print(b1.title)

        