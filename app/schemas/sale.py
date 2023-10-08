from pydantic import BaseModel
from datetime import datetime


class SaleSchema(BaseModel):
    product_id: int
    quantity: int
    total_price: float
    date_time: datetime
