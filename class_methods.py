class Book:

    Book_Types = ("Comic" , "Mystery" , "Adventurous")

    __Book_List = None

    @classmethod
    def getBookTypes(cls):
        return cls.Book_Types
    
    @staticmethod
    def getBookList():
        if Book.__Book_List == None:
            Book.__Book_List = []
        return Book.__Book_List


    def __init__(self , title , bookType):
        self.title= title
        if(not bookType in Book.Book_Types):
            return ValueError(f"{bookType} is not present")
        else:
            self.bookType = bookType

print(f"Book Types: {Book.getBookTypes()}")

book1 = Book("Good Education" , "Adventurous")
book2 = Book("playground" , "Mystery")

theBooks= Book.getBookList()
theBooks.append(book1)
theBooks.append(book2)
print(theBooks)

for item in theBooks:
    print(item.title)