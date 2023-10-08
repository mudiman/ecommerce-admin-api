"""add sequences

Revision ID: 1cb37288d520
Revises: ee5c955c039a
Create Date: 2023-10-08 15:33:44.400486

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1cb37288d520'
down_revision: Union[str, None] = 'ee5c955c039a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("CREATE SEQUENCE products_id_seq OWNED BY products.id")
    op.execute("CREATE SEQUENCE categories_id_seq OWNED BY categories.id")
    op.execute("CREATE SEQUENCE inventories_id_seq OWNED BY inventories.id")
    op.execute("CREATE SEQUENCE sales_id_seq OWNED BY sales.id")


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("DROP SEQUENCE products_id_seq")
    op.execute("DROP SEQUENCE categories_id_seq")
    op.execute("DROP SEQUENCE inventories_id_seq")
    op.execute("DROP SEQUENCE sales_id_seq")
