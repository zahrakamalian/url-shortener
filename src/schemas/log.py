from datetime import datetime

from pydantic import BaseModel, ConfigDict


class LogResponse(BaseModel):
    id: int
    clicked_at: datetime
    ip_address: str

    model_config = ConfigDict(from_attributes=True)
