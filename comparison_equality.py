class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __eq__(self, other):
        
        if(not isinstance(other, Book)):
            raise(ValueError("The comparison object is not the book object"))
        
        isSame =  (self.title == other.title and self.price == other.price)
        return isSame
           
    def __lt__(self, other):  
                
        if(not isinstance(other, Book)):
            raise(ValueError("The comparison object is not the book object"))   

        isLess = self.price < other.price   
        return isLess
    
    def __ge__(self, other):  
                
        if(not isinstance(other, Book)):
            raise(ValueError("The comparison object is not the book object"))   

        isLess = self.price >= other.price   
        return isLess

b1 = Book("Deep Learning", 50)
b2 = Book("Deep Learning", 50)
b3 = Book("Reinforcement", 100)
b4 = Book("ML CookBook", 30)
b5 = Book("The great gatsby", 500)

print(b1==b2)
print(b1==b4)

print(b1<b3)
print(b3<b4)

print(b3>=b2)
print(b2>=b3)

bookList = [b1, b2, b3, b4, b5]

bookList.sort()

for book in bookList:
    print(f"book price: {book.price}, book title = {book.title}")


print([book.price for book in bookList])