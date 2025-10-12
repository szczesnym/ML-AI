from domain.book import Book
from flask import session
from infrastructure.models import BookModel
from infrastructure.mapper.AuthorMapper import AuthorMapper
class BookMapper:
    @staticmethod
    def to_domain(book_model: BookModel) -> Book:
        if book_model is not None:
            book = Book(
                id=book_model.id,
                title=book_model.title,
                authors=book_model.authors,
                available=book_model.available
            )
            return book
        return None

    @staticmethod
    def to_model(book: Book, session) -> BookModel:
        if book.id is not None:
            existing = session.query(BookModel).get(book.id)
            if existing:
                return existing
        model_authors = [AuthorMapper.to_model(author=author, session=session) for author in book.authors]
        book_model = BookModel(
            title=book.title,
            authors=model_authors,
            available=book.available
        )
        return book_model


