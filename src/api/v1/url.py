from fastapi import APIRouter, Depends, status
from typing import Annotated, List


from src.api.dependencies import get_url_service, get_analytics_service
from src.services.url import URLService
from src.services.analytics import AnalyticsService
from src.schemas.url import CreateURLRequest, CreateURLResponse
from src.schemas.log import LogResponse

router = APIRouter()


@router.post("/", response_model=CreateURLResponse, status_code=status.HTTP_201_CREATED)
def create_short_url(request: CreateURLRequest,
                     service: Annotated[URLService, Depends(get_url_service)]):
    return service.create_short_url(request)


@router.get("/{url_id}/logs", response_model=List[LogResponse])
def get_url_logs(url_id: int,
                 service: Annotated[AnalyticsService, Depends(get_analytics_service)]):
    return service.get_logs(url_id)
