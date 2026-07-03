from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from src.db.session import get_db
from src.repositories.url import URLRepository
from src.repositories.log import LogRepository
from src.services.url import URLService
from src.services.analytics import AnalyticsService

DBSession = Annotated[Session, Depends(get_db)]


def get_url_repository(db: DBSession) -> URLRepository:
    return URLRepository(db)


def get_log_repository(db: DBSession) -> LogRepository:
    return LogRepository(db)


def get_url_service(url_repo: Annotated[URLRepository, Depends(get_url_repository)],
                    log_repo: Annotated[LogRepository, Depends(get_log_repository)]) -> URLService:
    return URLService(
        url_repository=url_repo,
        log_repository=log_repo,
    )


def get_analytics_service(url_repo: Annotated[URLRepository, Depends(get_url_repository)],
                          log_repo: Annotated[LogRepository, Depends(get_log_repository)]) -> URLService:
    return AnalyticsService(
        url_repository=url_repo,
        log_repository=log_repo,
    )
