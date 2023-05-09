class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}"
    
    def __repr__(self):
        return f"Title--: {self.title}, Author--: {self.author}"

b1 = Book("Harry Potter", "JK Rowling")
print(b1.title)
print(b1.author)
print(b1)
print(type(b1))    
print(str(b1))
print(repr(b1))
