from app.db.session import SessionLocal
from app.models import Category  # Import your database model
from sqlalchemy import text  # Import the text function from SQLAlchemy


def seed_data():
    db = SessionLocal()

    sql_insert_block = """
    truncate table categories RESTART IDENTITY CASCADE;
    truncate table products RESTART IDENTITY CASCADE;
    truncate table inventories RESTART IDENTITY CASCADE;
    truncate table sales RESTART IDENTITY CASCADE;

    INSERT INTO categories (id, name, description)
    VALUES
        (1, 'electronics', 'Gagets stuff'),
        (2, 'apparels', 'Clothing')
    ON CONFLICT DO NOTHING; 

    INSERT INTO products (id, name, description, category_id, price)
    VALUES
        (1, 'iphone', '', 1, 200),
        (2, 'samsung', '', 1, 100),
        (3, 'Green shirt', '', 2, 20),
        (4, 'Blue pant', '', 2, 10)
    ON CONFLICT DO NOTHING; 

    INSERT INTO inventories (id, product_id, quantity)
    VALUES
        (1, 1, 10),
        (2, 2, 5),
        (3, 3, 6),
        (4, 4, 7)
    ON CONFLICT DO NOTHING; 

    INSERT INTO sales (id, product_id, quantity, total_price, date_time)
    VALUES
        (1, 1, 2, 400, '2023-10-07'),
        (2, 2, 1, 100,'2023-10-08'),
        (3, 3, 4, 80,'2023-10-10'),
        (4, 4, 3, 30, '2023-10-11')
    ON CONFLICT DO NOTHING; 
    """
    sql_text = text(sql_insert_block)

    db.execute(sql_text)

    db.commit()
    db.close()


seed_data()
