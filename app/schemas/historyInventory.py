from pydantic import BaseModel
from datetime import datetime


class HistoryInventorySchema(BaseModel):
    product_id: int
    quantity: int
    updated_at: datetime
    description: str
