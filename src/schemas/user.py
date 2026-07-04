from pydantic import BaseModel
from typing import List


class UserHistoryResponse(BaseModel):
    user_id: int
    received_campaign_ids: List[int]
    opened_campaign_ids: List[int]
