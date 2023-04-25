class Book:
    
    def __init__(self , title1, author1):
        self.title = title1
        self.author = author1

b1 = Book("The secret" , "Ronalod")  
b2 = Book("Harry Potter" , "Jk Rowling")  
print(b1.author)
print(b2.title)