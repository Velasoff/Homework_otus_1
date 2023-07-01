"""add_index_for_names

Revision ID: f1ffb4b41bb7
Revises: d78d1469c014
Create Date: 2023-07-01 15:17:05.131193

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "f1ffb4b41bb7"
down_revision = "d78d1469c014"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(
        """
            CREATE EXTENSION pg_trgm;
            CREATE INDEX idx_users_sn_fn ON users USING GIN (second_name, first_name);
        """
    )


def downgrade() -> None:
    op.execute("DROP INDEX IF EXISTS idx_users_sn_fn;")
