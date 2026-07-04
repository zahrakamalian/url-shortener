from fastapi import APIRouter, Depends
from typing import Annotated

from src.api.dependencies import get_analytics_service
from src.services.analytics import AnalyticsService
from src.schemas.campaign import CampaignStatsResponse
from src.schemas.user import UserHistoryResponse

router = APIRouter()


@router.get("/campaigns/{campaign_id}/stats", response_model=CampaignStatsResponse)
def get_campaign_stats(campaign_id: int,
                       service: Annotated[AnalyticsService, Depends(get_analytics_service)]):
    return service.get_campaign_stats(campaign_id)


@router.get("/users/{user_id}/urls", response_model=UserHistoryResponse)
def get_user_history(user_id: int,
                     service: Annotated[AnalyticsService, Depends(get_analytics_service)]):
    return service.get_user_history(user_id)
