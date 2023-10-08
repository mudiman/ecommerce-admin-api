from pydantic import BaseModel
from datetime import datetime


class InventorySchema(BaseModel):
    product_id: int
    quantity: int
    crated_at: datetime
