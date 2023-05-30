"""add_token_table

Revision ID: d78d1469c014
Revises: 1217fbae61af
Create Date: 2023-05-15 17:57:06.815009

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "d78d1469c014"
down_revision = "1217fbae61af"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(
        """
            CREATE TABLE IF NOT EXISTS tokens(
                id SERIAL PRIMARY KEY,
                user_id VARCHAR(100) NOT NULL,
                token VARCHAR(100) NOT NULL,
                expired_at TIMESTAMP NOT NULL
            );
        """
    )


def downgrade() -> None:
    op.execute("DROP TABLE IF EXISTS tokens;")
