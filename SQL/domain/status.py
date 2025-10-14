import datetime
from .book import Book

class Status:
    def __init__(self, book: Book, status: int, timestamp=None, id=0):
        self.id = id
        self.status = status #0 - OUT, 1 - IN
        self.book = book
        if not timestamp:
            self.timestamp = datetime.datetime.now()
        else:
            self.timestamp = timestamp
    def __repr__(self):
        return f'<Status(id={self.id}, book_id:={self.book.id}, status={self.status}, timestamp={self.timestamp})>'