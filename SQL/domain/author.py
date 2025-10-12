class Author:
    def __init__(self, first_name: str, last_name: str, id: int = None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.books = []

    def __repr__(self):
        return f'ID:{self.id}, First Name:{self.first_name}, Family Name:{self.last_name}'