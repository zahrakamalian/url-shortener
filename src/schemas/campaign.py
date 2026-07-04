from pydantic import BaseModel


class CampaignStatsResponse(BaseModel):
    campaign_id: int
    sent_count: int
    opened_count: int
    conversion_rate: float
