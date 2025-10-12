from book import Book
from status import Status
class Library:
    def __init__(self):
        super.__init__(self)
        self.library =list[Book]

    def get_library(self):
        return self.library

    def add_book(self, book: Book):
        self.library.append(book)

    def rent_book(self, book: Book) -> bool:
        if book in self.library:
            book.available = False
            return True
        else:
            return False

    def return_book(self, book: Book) -> bool:
        if book in self.library:
            book.available = True
            return True
        else:
            return False
