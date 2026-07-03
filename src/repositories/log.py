from sqlalchemy.orm import Session
from typing import List

from src.db.models.log import Log


class LogRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_log(self, log: Log) -> Log:
        self.db.add(log)
        self.db.commit()
        self.db.refresh(log)
        return log

    def rollback(self) -> None:
        self.db.rollback()

    def get_logs_by_url_id(self, url_id: int) -> List[Log]:
        return self.db.query(Log).filter(Log.url_id == url_id).all()
