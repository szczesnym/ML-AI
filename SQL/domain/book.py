from .author import Author


class Book:
    def __init__(self, title: str, authors: list | None, id: int = None, available: bool = True):
        self.id  = id
        self.title = title
        self.available = available
        #TU był -> WITAW CHAT GPP
        #self.authors = authors
        if authors is None:
            self.authors = []
        else:
            self.authors = [author for author in authors]

    def add_author(self, author):
        self.authors.append(author)

    def __repr__(self):
        return f'ID:{self.id}, Title:{self.title}, Authors:{self.authors}, Available:{self.available}'


