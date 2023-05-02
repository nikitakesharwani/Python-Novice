class Media:
    def __init__(self, title, price):
        self.title = title
        self.price = price

class Publication(Media):
    def __init__(self, title, price, period, publisher):
        super().__init__(title, price)
        self.period = period
        self.publisher =publisher

class Book(Media):
    def __init__(self, title, price, author, pages):
        super().__init__(title, price)
        self.author = author
        self.pages = pages

class Magzine(Publication):
    def __init__(self, title, price, period, publisher):
        super().__init__(title, price, period, publisher)

class Newspaper(Publication):
    def __init__(self, title, price, period, publisher):
        super().__init__(title, price, period, publisher)

book1 = Book("Beast", 100 , "Charles Nick", 299)
magzine1 = Magzine("Haze", 500, 4.5, "Niks Publication")
newspaper1 = Newspaper("War", 237, 1.4, "Hira Publication")

print(book1.author)
print(newspaper1.period)
print(magzine1.publisher)