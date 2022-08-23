"""currency table

Revision ID: f1115b2334e1
Revises: 98d9d323809e
Create Date: 2022-08-23 10:04:54.547058

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f1115b2334e1'
down_revision = '98d9d323809e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "currency",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("code", sa.String, nullable=False, unique=True, index=True),
        sa.Column("name", sa.String, nullable=False, unique=True)
    )


def downgrade() -> None:
    op.drop_table("currency")
