from fastapi import APIRouter

from app.api.endpoints import sales, products, revenue, inventory

api_router = APIRouter()
api_router.include_router(sales.router, prefix="/sales", tags=["sales"])
api_router.include_router(
    products.router, prefix="/products", tags=["products"])
api_router.include_router(revenue.router, prefix="/revenue", tags=["revenue"])
api_router.include_router(
    inventory.router, prefix="/inventories", tags=["inventories"])
