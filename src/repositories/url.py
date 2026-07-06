from sqlalchemy.orm import Session
from sqlalchemy import update

from src.db.models.url import URL
from src.db.models.log import Log


class URLRepository():
    def __init__(self, db: Session):
        self.db = db

    def add(self, url: URL) -> URL:
        self.db.add(url)
        return url

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

    def increment_views(self, url_id: int) -> None:
        self.db.execute(update(URL).where(
            URL.id == url_id).values(views=URL.views + 1))
