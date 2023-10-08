from pydantic import BaseModel


class ProductSchema(BaseModel):
    name: str
    category_id: int
    description: str
    price: float
