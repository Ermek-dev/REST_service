"""create tasks table

Revision ID: c2ae3f246b33
Revises: 783ef95430fe
Create Date: 2025-09-19 05:07:25.402294

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c2ae3f246b33'
down_revision: Union[str, Sequence[str], None] = '783ef95430fe'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
