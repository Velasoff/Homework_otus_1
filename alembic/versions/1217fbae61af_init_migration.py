"""init_migration

Revision ID: 1217fbae61af
Revises: 
Create Date: 2023-05-14 13:00:34.006081

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1217fbae61af'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(100) NOT NULL,
            last_name VARCHAR(100) NOT NULL,
            age INT NOT NULL,
            sex BOOLEAN NOT NULL,
            interests TEXT,
            city VARCHAR(100)
        );
    """)


def downgrade() -> None:
    op.execute("DROP TABLE users;")