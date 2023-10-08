# models.py
from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

from app.db.base_class import Base


# Historical Inventory Model
class HistoricalInventory(Base):
    __tablename__ = "historical_inventory"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('inventory.id'))
    quantity = Column(Integer)
    updated_at = Column(DateTime, default=datetime.utcnow)

    history = relationship("Inventory", back_populates="historical_entries")
