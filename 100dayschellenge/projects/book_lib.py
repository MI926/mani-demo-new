class lib_book():
    def __init__(self):
        self.no_book = 0
        self.books = []  
    def addbook(self, book):
        self.no_book += 1
        self.books.append(book)
    def show(self):
        print(f"no of books is {self.no_book}")
        for book in self.books:
            print(book)
a = lib_book()
a.addbook("harry potterh")
a.addbook("harry potterujg")
a.addbook("harry potterwrg")
a.addbook("harry potterq34t")
a.addbook("harry pottertrhny")
a.addbook("harry potterqrtg")
a.show()
