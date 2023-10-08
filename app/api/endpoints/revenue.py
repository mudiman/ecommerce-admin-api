from fastapi import Query, Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import func
import datetime

from app.db.session import get_db
from app import models

router = APIRouter()


def productFilter(product_id, query):
    if product_id:
        query = query.filter(models.Sale.product_id == product_id)
    return query


def categoryFilter(category_id, query):
    if category_id:
        query = query.join(models.Product).filter(
            models.Product.category_id == category_id)
    return query


@router.get("/daily")
async def get_daily_revenue(
        category_id: int = Query(None, description="Filter by category id"),
        product_id: int = Query(None, description="Filter by product id"),
        db: Session = Depends(get_db)):
    today = datetime.date.today()
    query = db.query(func.sum(models.Sale.total_price)).filter(
        models.Sale.date_time == today)

    query = productFilter(product_id, query)
    query = categoryFilter(category_id, query)

    return {"revenue": query.scalar() or 0}


@router.get("/weekly")
async def get_weekly_revenue(
        category_id: int = Query(None, description="Filter by category id"),
        product_id: int = Query(None, description="Filter by product id"),
        db: Session = Depends(get_db)):
    start_date = datetime.date.today() - datetime.timedelta(days=7)
    end_date = datetime.date.today()
    query = db.query(func.sum(models.Sale.total_price)).filter(
        models.Sale.date_time.between(start_date, end_date)).scalar()

    query = productFilter(product_id, query)
    query = categoryFilter(category_id, query)

    return {"revenue": query.scalar() or 0}


@router.get("/monthly")
async def get_monthly_revenue(
        category_id: int = Query(None, description="Filter by category id"),
        product_id: int = Query(None, description="Filter by product id"),
        db: Session = Depends(get_db)):
    today = datetime.date.today()
    start_date = datetime.date(today.year, today.month, 1)
    end_date = today
    query = db.query(func.sum(models.Sale.total_price)).filter(
        models.Sale.date_time.between(start_date, end_date)).scalar()

    query = productFilter(product_id, query)
    query = categoryFilter(category_id, query)

    return {"revenue": query.scalar() or 0}


@router.get("/annual")
async def get_annual_revenue(
        category_id: int = Query(None, description="Filter by category id"),
        product_id: int = Query(None, description="Filter by product id"),
        db: Session = Depends(get_db)):
    today = datetime.date.today()
    start_date = datetime.date(today.year, 1, 1)
    end_date = today
    query = db.query(func.sum(models.Sale.total_price)).filter(
        models.Sale.date_time.between(start_date, end_date)).scalar()

    query = productFilter(product_id, query)
    query = categoryFilter(category_id, query)

    return {"revenue": query.scalar() or 0}
