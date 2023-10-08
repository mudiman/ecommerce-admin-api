# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa
from app.models.category import Category
from app.models.product import Product
from app.models.sale import Sale
from app.models.inventory import Integer
