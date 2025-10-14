from ..domain.author import Author
from ..infrastructure.models import AuthorModel

class AuthorRepository:
    def __init__(self, session, mapper):
        self.session = session
        self.mapper = mapper

    def get_all(self) -> list[Author]:
        model_authors = self.session.query(AuthorModel).all()
        return [self.mapper.to_domain(model_author) for model_author in model_authors]

    def get_by_str(self, first_name: str, last_name: str) -> Author:
        model_author = self.session.query(AuthorModel).filter_by(first_name=first_name, last_name=last_name).first()
        if model_author:
            return self.mapper.to_domain(model_author)
        return None

    def add(self, author: Author) -> int:
        model_author = self.mapper.to_model(author, self.session)
        self.session.add(model_author)
        self.session.commit()
        return model_author.id
