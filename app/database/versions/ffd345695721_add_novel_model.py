"""Add Novel Model

Revision ID: ffd345695721
Revises: 54e8ea53d606
Create Date: 2024-08-05 20:02:27.662126

"""

import datetime
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "ffd345695721"
down_revision: Union[str, None] = "54e8ea53d606"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "novel",
        sa.Column(
            "id",
            sa.Integer,
            primary_key=True,
            nullable=False,
            unique=True,
            autoincrement=True,
        ),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text, nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime,
            nullable=False,
            default=datetime.datetime.now(),
        ),
        sa.Column(
            "updated_at",
            sa.DateTime,
            nullable=False,
            default=datetime.datetime.now(),
        ),
    )
    op.add_column("user", sa.Column("novel_id", sa.Integer, nullable=True))
    op.create_foreign_key(
        "novel_user_fk",
        source_table="user",
        referent_table="novel",
        local_cols=["novel_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )


def downgrade() -> None:
    op.drop_column("user", "novel")
    op.drop_table("novel")
