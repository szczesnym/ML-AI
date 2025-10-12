from unit1.SQL.domain.status import Status
from unit1.SQL.infrastructure.models import StatusModel
#from unit1.SQL.infrastructureAuthorMapper import AuthorMapper

class StatusMapper:
    @staticmethod
    def to_domain(status: StatusModel) -> Status:
        status = Status(
            id=status.id,
            book=status.book,
            status=status.status,
            timestamp=status.timestamp
        )
        return status

    @staticmethod
    def to_model(status: Status) -> StatusModel:
        model_status = StatusModel(
            timestamp=status.timestamp,
            book_id=status.book.id,
            status=status.status
        )
        return model_status


