from sqlalchemy.orm import Session

from src.db.models.url import URL
from src.db.models.log import Log


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

    def get_by_id(self, url_id: int) -> URL | None:
        return self.db.query(URL).filter(URL.id == url_id).first()

    def count_by_campaign(self, campaign_id: int) -> int:
        return self.db.query(URL).filter(URL.campaign_id == campaign_id).count()

    def count_opened_by_campaign(self, campaign_id: int) -> int:
        return self.db.query(URL).join(Log, Log.url_id == URL.id).filter(URL.campaign_id == campaign_id).distinct(URL.id).count()

    def get_received_campaigns(self, user_id: int) -> list[int]:
        rows = self.db.query(URL.campaign_id).filter(
            URL.user_id == user_id).distinct().all()
        return [row[0] for row in rows]

    def get_opened_campaigns(self, user_id: int) -> list[int]:
        rows = self.db.query(URL.campaign_id).join(Log, Log.url_id == URL.id).filter(
            URL.user_id == user_id).distinct().all()
        return [row[0] for row in rows]
