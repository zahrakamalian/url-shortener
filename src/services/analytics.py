from typing import List
from fastapi import HTTPException, status

from src.repositories.url import URLRepository
from src.repositories.log import LogRepository
from src.schemas.log import LogResponse


class AnalyticsService:
    def __init__(self, url_repository: URLRepository, log_repository: LogRepository):
        self.url_repo = url_repository
        self.log_repo = log_repository

    def get_logs(self, url_id: int) -> List[LogResponse]:
        url = self.url_repo.get_by_id(url_id)
        if not url:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="URL not found.")

        logs = self.log_repo.get_logs_by_url_id(url_id)
        return logs
