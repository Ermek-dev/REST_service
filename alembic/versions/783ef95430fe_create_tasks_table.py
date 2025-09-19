"""create tasks table

Revision ID: 783ef95430fe
Revises:
Create Date: 2025-09-19 04:28:55.893090
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '783ef95430fe'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Upgrade schema: create tasks table."""
    op.create_table(
        "tasks",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text, nullable=True),
        sa.Column("status", sa.String(length=50), nullable=False, server_default="todo"),
        sa.Column("created_at", sa.DateTime, server_default=sa.func.now(), nullable=False),
        sa.Column("updated_at", sa.DateTime, server_default=sa.func.now(), onupdate=sa.func.now(), nullable=False),
    )


def downgrade() -> None:
    """Downgrade schema: drop tasks table."""
    op.drop_table("tasks")
