from unit1.SQL.domain.book import Book
from unit1.SQL.domain.author import Author
from unit1.SQL.repositories.AuthorRepository import AuthorRepository
from unit1.SQL.repositories.BookRepository import BookRepository


class LibraryService:
    def __init__(self, library: BookRepository, authors: AuthorRepository ):
        self.library = library
        self.authors = authors

    def add_by_str(self, book_title: str, author_first_name: str, author_last_name: str) -> int:
        author = self.authors.get_by_str(first_name=author_first_name, last_name=author_last_name)
        if author :
            authors = [author]
        else :
            author = Author(first_name=author_first_name, last_name=author_last_name)
            authors = [author]
        book = Book(title=book_title, authors=authors)
        self.library.add(book)
        return book.id

    def add_book_author(self, book: Book, author: Author) -> Book:
        self.library.add(book)
        if author not in self.authors.get_all():
            self.authors.add(author)
        self.library.add_book_author(book, author)
        return book

    def rent(self, book: Book) -> Book:
        if book in self.library.get_all():
            book.available = False
        return self.library.rent(book=book)

#    def return_rent(self, book: Book) -> Book:
#        book_model = self.get_book_by_id(book.id)
#        if book_model is not None:
#            book_model.available = True
#            status_model = StatusModel(book_id=book_model.id, status=1)
#            self.session.add(status_model)
#            self.session.commit()
#        return book_model_to_domain(self.get_book_by_id(book_model.id))
