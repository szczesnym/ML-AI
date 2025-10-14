from ..domain import Book, Author, Status
from ..infrastructure.models import AuthorModel, BookModel
from ..infrastructure.mapper.StatusMapper import StatusMapper
from ..repositories import StatusRepository

class BookRepository:
    def __init__(self, session, mapper):
        self.session = session
        self.mapper = mapper

    def get_all(self) -> list[Book]:
        model_books = self.session.query(BookModel).all()
        if model_books:
            return [self.mapper.to_domain(book_model=model_book) for model_book in model_books]
        else:
            return None

    def get_by_id(self, book_id) -> Book:
        model_book = self.session.query(BookModel).get(book_id)
        return self.mapper.to_domain(book_model=model_book)

    def add(self, book: Book) -> Book:
        book_model = self.mapper.to_model(book, self.session)
        self.session.add(book_model)
        self.session.commit()
        return self.mapper.to_domain(book_model=book_model)

    def add_book_author(self, book: Book, author: Author) -> int:
        if author.id is not None:
            model_author = self.session.query(AuthorModel).get(author.id)
        else:
            return -1
        model_book = self.mapper.to_model(book, self.session)
        model_book.authors.append(model_author)
        self.session.commit()
        return model_book.id

    def rent(self, book: Book) -> Book:
        if self.get_by_id(book.id):
            status_repo = StatusRepository(self.session, StatusMapper)
            status = Status(book=book, status=0)
            status_repo.add(status)
            model_book = self.session.query(BookModel).get(book.id)
            model_book.available = False
            self.session.commit()
            return self.get_by_id(book_id=model_book.id)
        return None
