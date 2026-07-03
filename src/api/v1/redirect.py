from fastapi import APIRouter, Depends, status, Request
from fastapi.responses import RedirectResponse
from typing import Annotated

from src.api.dependencies import get_url_service
from src.services.url import URLService

router = APIRouter()


@router.get("/{short_code}", status_code=status.HTTP_302_FOUND)
def redirect(short_code: str,
             request: Request,
             service: Annotated[URLService, Depends(get_url_service)]):

    ip = request.client.host if request.client else "unknown"
    original_url = service.redirect(short_code, ip)
    return RedirectResponse(original_url)
