"""bank_list table

Revision ID: 98d9d323809e
Revises: 580547615c64
Create Date: 2022-08-22 19:35:25.635836

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98d9d323809e'
down_revision = '580547615c64'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "bank_list",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("name", sa.String, nullable=False, unique=True, index=True),
        sa.Column("mfo", sa.Integer, unique=True),
        sa.Column("edrpou", sa.Integer, unique=True),
        sa.Column("ipn", sa.BigInteger, unique=True),
        sa.Column("iban", sa.String, unique=True),
        sa.Column("swift", sa.String, unique=True)
    )


def downgrade() -> None:
    op.drop_table("bank_list")
