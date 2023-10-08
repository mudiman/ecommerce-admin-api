from datetime import date
import pytest
from fastapi import Depends
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session, sessionmaker
from main import app
from app.db.session import get_db, engine
from app.models import Sale

client = TestClient(app)


@pytest.fixture
def db_session():
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def test_get_daily_revenue(monkeypatch, db_session: Session):
    expected_revenue = 100
    monkeypatch.setattr(db_session.query(Sale), 'scalar',
                        lambda: expected_revenue)

    response = client.get("/api/v1/revenue/daily")
    assert response.status_code == 200
    assert response.json() == {"revenue": expected_revenue}


def test_get_daily_revenue_by_product_id(monkeypatch, db_session: Session):
    expected_revenue = 0
    product_id = 1

    # Mock the query to filter by product_id
    def mock_query_product_id(*args, **kwargs):
        return db_session.query(Sale).filter(Sale.product_id == product_id).scalar()

    monkeypatch.setattr(db_session.query(
        Sale), 'scalar', mock_query_product_id)

    # response = client.get(
    #     f"/api/v1/revenue/daily?product_id={product_id}")
    response = client.get("/revenue/daily", params={"product_id": product_id})

    assert response.status_code == 200
    assert response.json() == {"revenue": expected_revenue}
