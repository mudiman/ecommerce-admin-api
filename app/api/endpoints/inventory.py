from fastapi import HTTPException, Query, Depends
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
import datetime
from app.db.session import get_db
from app import models, schemas
from app.config.config import get_settings

settings = get_settings()

router = APIRouter()


class CreateInventorySchema(BaseModel):
    product_id: int
    quantity: int


@router.get("", response_model=list[schemas.InventorySchema])
async def get_low_inventories(
    db: Session = Depends(get_db)
):
    inventories = db.query(models.Inventory).filter(
        models.Inventory.quantity == settings.low_stock_threshold).all()
    return inventories


@router.post("", response_model=None)
async def create_product_inventory(inventory: CreateInventorySchema, db: Session = Depends(get_db)):
    try:
        # Create a new inventory instance
        new_inventory = models.inventory(
            product_id=inventory.product_id,
            quantity=inventory.quantity,
            created_at=datetime.utcnow()
        )

        # Save the new inventory to the database
        db.add(new_inventory)
        db.commit()
        db.refresh(new_inventory)

        return new_inventory
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/{product_id}")
async def update_product_inventory(product_id: int, inventory: schemas.InventorySchema, db: Session = Depends(get_db)):
    try:
        # Retrieve the existing inventory from the database using the provided inventory_id
        existing_inventory = db.query(models.inventory).filter(
            models.inventory.product_id == product_id).first()

        if existing_inventory:
            # Save the current inventory quantity as historical entry
            historical_entry = models.HistoricalInventory(
                product_id=existing_inventory.product_id,
                quantity=existing_inventory.quantity,
                updated_at=existing_inventory.created_at
            )
            db.add(historical_entry)
            existing_inventory.quantity = inventory.quantity

            db.commit()
            return existing_inventory
        else:
            raise HTTPException(status_code=404, detail="inventory not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{inventory_id}")
async def delete_inventory(inventory_id: int, db: Session = Depends(get_db)):
    try:
        # Retrieve the inventory from the database by the provided inventory_id
        inventory_to_delete = db.query(models.inventory).filter(
            models.inventory.id == inventory_id).first()

        if inventory_to_delete:
            # Remove the inventory from the database
            db.delete(inventory_to_delete)
            db.commit()
            return {"message": "inventory deleted successfully"}
        else:
            raise HTTPException(status_code=404, detail="inventory not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/history/{product_id}", response_model=list[schemas.HistoryInventorySchema])
async def get_product_inventory_history(
    product_id: int,
    db: Session = Depends(get_db)
):
    inventories = db.query(models.HistoricalInventory).filter(
        models.HistoricalInventory.product_id == product_id).all()
    return inventories
