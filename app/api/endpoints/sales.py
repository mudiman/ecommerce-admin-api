from fastapi import HTTPException, Query, Depends
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
import datetime

from app.db.session import get_db
from app import models, schemas

router = APIRouter()


@router.get("", response_model=list[schemas.SaleSchema])
async def get_sales(
    start_date: datetime.date = Query(None),
    end_date: datetime.date = Query(None),
    product_id: int = Query(None, description="Filter by product id"),
    category_id: int = Query(None, description="Filter by category id"),
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    query = db.query(models.Sale)
    if product_id:
        query = query.filter(models.Sale.product_id == product_id)
    if category_id:
        query = query.join(models.Product).filter(
            models.Product.category_id == category_id)

    if start_date:
        query = query.filter(
            func.date(models.Sale.start_date) >= func.date(start_date))
    if end_date:
        query = query.filter(
            func.date(models.Sale.end_date) < func.date(end_date))

    sales = query.offset(skip).limit(limit).all()
    return sales


@router.get("/{sale_id}", response_model=schemas.SaleSchema)
async def get_sale_by_id(sale_id: int, db: Session = Depends(get_db)):
    sale = db.query(models.Sale).filter(models.Sale.id == sale_id).first()
    if sale is None:
        raise HTTPException(status_code=404, detail="Sale not found")
    return sale
