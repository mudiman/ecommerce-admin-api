from fastapi import HTTPException, Query, Depends
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.db.session import get_db
from app import models, schemas

router = APIRouter()


class CreateProductRequest(BaseModel):
    name: str
    description: str
    category_id: int
    price: float


@router.get("", response_model=list[schemas.ProductSchema])
async def get_products(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    products = db.query(models.Product).offset(skip).limit(limit).all()
    return products


@router.post("", response_model=None)
async def create_product(product: CreateProductRequest, db: Session = Depends(get_db)):
    try:
        # Create a new product instance
        new_product = models.Product(
            name=product.name,
            category_id=product.category_id,
            price=product.price,
            description=product.description
        )

        # Save the new product to the database
        db.add(new_product)
        db.commit()
        db.refresh(new_product)

        return new_product
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/{product_id}")
async def update_product(product_id: int, product: schemas.ProductSchema, db: Session = Depends(get_db)):
    try:
        # Retrieve the existing product from the database using the provided product_id
        existing_product = db.query(models.Product).filter(
            models.Product.id == product_id).first()

        if existing_product:
            # Update the attributes of the retrieved product with the new product data
            existing_product.name = product.name
            existing_product.category_id = product.category_id
            existing_product.price = product.price
            existing_product.description = product.description

            # Save the updated product back to the database
            db.commit()
            return existing_product
        else:
            raise HTTPException(status_code=404, detail="Product not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{product_id}")
async def delete_product(product_id: int, db: Session = Depends(get_db)):
    try:
        # Retrieve the product from the database by the provided product_id
        product_to_delete = db.query(models.Product).filter(
            models.Product.id == product_id).first()

        if product_to_delete:
            # Remove the product from the database
            db.delete(product_to_delete)
            db.commit()
            return {"message": "Product deleted successfully"}
        else:
            raise HTTPException(status_code=404, detail="Product not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
