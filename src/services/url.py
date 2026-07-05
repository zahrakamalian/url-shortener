from nanoid import generate
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from src.repositories.url import URLRepository
from src.repositories.log import LogRepository
from src.schemas.url import CreateURLRequest, CreateURLResponse
from src.db.models.url import URL
from src.db.models.log import Log

SHORT_CODE_LENGTH = 7
MAX_RETRIES = 3


def generate_short_code() -> str:
    return generate(size=SHORT_CODE_LENGTH)


class URLService:
    def __init__(self, db: Session, url_repository: URLRepository, log_repository: LogRepository):
        self.db = db
        self.url_repo = url_repository
        self.log_repo = log_repository

    def create_short_url(self, request: CreateURLRequest) -> CreateURLResponse:
        for _ in range(MAX_RETRIES):
            url_entry = URL(
                user_id=request.user_id,
                campaign_id=request.campaign_id,
                original_url=str(request.original_url),
                short_code=generate_short_code()
            )
            try:
                created_url = self.url_repo.add(url_entry)
                self.db.commit()
                return CreateURLResponse(
                    short_code=created_url.short_code
                )

            except IntegrityError:
                self.db.rollback()

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Could not generate a unique short code."
        )

    def redirect(self, short_code: str, ip: str) -> str:
        url = self.url_repo.get_by_short_code(short_code)
        if not url:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Invalid link."
            )

        try:
            with self.db.begin():
                log_entry = Log(
                    url_id=url.id,
                    ip_address=ip,
                )

                self.log_repo.add(log_entry)
                self.url_repo.increment_views(url)

        except IntegrityError:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to update URL statistics."
            )

        return url.original_url
