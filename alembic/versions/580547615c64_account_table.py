"""account table

Revision ID: 580547615c64
Revises: 
Create Date: 2022-08-22 11:15:44.276272

"""
from alembic import op
import sqlalchemy as sa
import secrets


# revision identifiers, used by Alembic.
revision = '580547615c64'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "account",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("name", sa.VARCHAR(30), nullable=False, unique=True),
        sa.Column("email", sa.String, nullable=False, unique=True),
        sa.Column("password", sa.String, nullable=False),
        sa.Column("is_active", sa.BOOLEAN, default=True),
        sa.Column("is_admin", sa.BOOLEAN, default=False),
        sa.Column("registered_at", sa.DateTime, server_default=sa.func.now()),
        sa.Column("api_key", sa.String, unique=True, default=secrets.token_urlsafe, index=True)
    )


def downgrade() -> None:
    op.drop_table("account")
