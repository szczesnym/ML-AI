import datetime

from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Table, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker, declarative_base
from .database import Base

book_author = Table(
    'book_author',
    Base.metadata,
    Column('book_id', Integer, ForeignKey('book.id')),
    Column('author_id', Integer, ForeignKey('author.id'))
)

class BookModel(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    available = Column(Boolean, nullable=False)
    authors = relationship('AuthorModel', back_populates='books',secondary=book_author)


class AuthorModel(Base):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    books = relationship('BookModel', back_populates='authors', secondary=book_author)
    __table_args__ = (UniqueConstraint("first_name", "last_name", name="first_name_last_name"),)
    def __repr__(self):
        return "<AuthorModel(id=%d, first_name=%s, last_name=%s)>" % (self.id, self.first_name, self.last_name)

class StatusModel(Base):
    __tablename__ = 'statuses'
    id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(DateTime, nullable=False)
    status = Column(Integer, nullable=False) #0 - OUT, 1 - IN
    book_id = Column(Integer, ForeignKey('book.id'))
    book = relationship('BookModel', backref='status')

    def __init__(self, book_id: int, status: int, timestamp: datetime.datetime):
        self.book_id = book_id
        self.timestamp = datetime.datetime.now()
        self.status = status


