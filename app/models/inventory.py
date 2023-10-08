# models.py
from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

from app.db.base_class import Base


class Inventory(Base):
    __tablename__ = 'inventories'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    product = relationship('Product', back_populates='inventory')
    quantity = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)

    history = relationship('HistoryInventories', back_populates='inventory')
