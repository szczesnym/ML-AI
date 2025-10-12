from unit1.SQL.domain.status import Status


class StatusRepository:
    def __init__(self, session, mapper):
        self.session = session
        self.mapper = mapper

    def add(self, status: Status) -> int:
        model_status = self.mapper.to_model(status=status)
        self.session.add(model_status)
        self.session.commit()
        return model_status.id

    def get_by_book_id(self, status: Status, book_id: int) -> list[Status]:
        return [self.mapper.to_domain(model_status) for model_status in self.session.query(StatusModel).filter_by(book_id=book.id)]
