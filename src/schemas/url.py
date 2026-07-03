from pydantic import BaseModel, HttpUrl


class CreateURLRequest(BaseModel):
    user_id: int
    campaign_id: int
    original_url: HttpUrl


class CreateURLResponse(BaseModel):
    short_code: str
