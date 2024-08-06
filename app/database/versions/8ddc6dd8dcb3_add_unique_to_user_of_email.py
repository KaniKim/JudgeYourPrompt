"""Add unique to user of email

Revision ID: 8ddc6dd8dcb3
Revises: ffd345695721
Create Date: 2024-08-06 22:23:24.033635

"""

from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "8ddc6dd8dcb3"
down_revision: Union[str, None] = "ffd345695721"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_unique_constraint("unique_email", "user", ["email"])


def downgrade() -> None:
    op.drop_constraint("unique_email", "user", type_="unique")
