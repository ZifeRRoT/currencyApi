"""exchange_rates table

Revision ID: 7f47f657ebf4
Revises: f1115b2334e1
Create Date: 2022-08-23 10:09:05.083580

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f47f657ebf4'
down_revision = 'f1115b2334e1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "exchange_rates",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("bak_id", sa.Integer, sa.ForeignKey("bank_list.id")),
        sa.Column("currency_id", sa.Integer, sa.ForeignKey("currency.id")),
        sa.Column("purchase", sa.Float, nullable=False),
        sa.Column("sale", sa.Float, nullable=False),
        sa.Column("date", sa.Date, server_default=sa.func.now())
    )


def downgrade() -> None:
    op.drop_table("exchange_rates")
