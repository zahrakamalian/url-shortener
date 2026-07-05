from sqlalchemy.orm import Session
from typing import List

from src.db.models.log import Log


class LogRepository:
    def __init__(self, db: Session):
        self.db = db

    def add(self, log: Log) -> None:
        self.db.add(log)

    def get_logs_by_url_id(self, url_id: int) -> List[Log]:
        return self.db.query(Log).filter(Log.url_id == url_id).all()
