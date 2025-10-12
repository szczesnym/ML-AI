#from sqlalchemy import create_engine
#from sqlalchemy.orm import sessionmaker, declarative_base
#from infrastructure import models
import random
from infrastructure.database import SessionLocal, Base, engine
from unit1.SQL.infrastructure.LibraryApp import LibraryApp

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    session = SessionLocal()
    library = LibraryApp(session=session)
    if not library.books.get_all():
        library.initialize()
    print(library.books.get_all())

    random_book = random.choice(library.books.get_all())
    print(f'Random book:{random_book}')
    print(f'After book rent {library.books.rent(random_book)}')
    #print(f'After book return {library.return_rent(random_book)}')
    #print(f'List of circulation of book {library.get_book_status_all(random_book)}')
    #random_author = random.choice(library.get_all_authors())
    #print(f'Random Author:{random_author}')
    #print(f'Add random author to book: {library.add_book_author(random_book, random_author)}')

