from fastapi import HTTPException, status

from src.repositories.url import URLRepository
from src.repositories.log import LogRepository
from src.schemas.log import LogResponse
from src.schemas.campaign import CampaignStatsResponse
from src.schemas.user import UserHistoryResponse


class AnalyticsService:
    def __init__(self, url_repository: URLRepository, log_repository: LogRepository):
        self.url_repo = url_repository
        self.log_repo = log_repository

    def get_logs(self, url_id: int) -> list[LogResponse]:
        url = self.url_repo.get_by_id(url_id)
        if not url:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="URL not found.")

        logs = self.log_repo.get_logs_by_url_id(url_id)
        return logs

    def get_campaign_stats(self, campaign_id: int) -> CampaignStatsResponse:
        sent_count = self.url_repo.count_by_campaign(campaign_id)
        opened_count = self.url_repo.count_opened_by_campaign(campaign_id)

        return CampaignStatsResponse(
            campaign_id=campaign_id,
            sent_count=sent_count,
            opened_count=opened_count,
            conversion_rate=((opened_count / sent_count) * 100
                             if sent_count > 0
                             else 0.0
                             )
        )

    def get_user_history(self, user_id: int) -> UserHistoryResponse:
        received_campaigns = self.url_repo.get_received_campaigns(user_id)
        opened_campaigns = self.url_repo.get_opened_campaigns(user_id)

        return UserHistoryResponse(
            user_id=user_id,
            received_campaign_ids=received_campaigns,
            opened_campaign_ids=opened_campaigns
        )
