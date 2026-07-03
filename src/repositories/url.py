from sqlalchemy.orm import Session

from src.db.models.url import URL


class URLRepository():
    def __init__(self, db: Session):
        self.db = db

    def create_url(self, url: URL) -> URL:
        self.db.add(url)
        self.db.commit()
        self.db.refresh(url)
        return url

    def rollback(self) -> None:
        self.db.rollback()

    def get_by_short_code(self, short_code: str) -> URL | None:
        return self.db.query(URL).filter(URL.short_code == short_code).first()

    def get_by_id(self, url_id) -> URL | None:
        return self.db.query(URL).filter(URL.id == url_id).first()
