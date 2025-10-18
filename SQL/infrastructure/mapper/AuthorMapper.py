from ...domain.author import Author
from ..models import AuthorModel


class AuthorMapper:
    @staticmethod
    def to_model(author: Author, session) -> AuthorModel:
        existing = session.query(AuthorModel).filter_by(first_name=author.first_name, last_name=author.last_name).first()
        if existing:
            return existing
        return AuthorModel(
            first_name=author.first_name,
            last_name=author.last_name
        )

    @staticmethod
    def to_domain(author: AuthorModel) -> Author:
        return Author(
            id=author.id,
            first_name=author.first_name,
            last_name=author.last_name
        )

