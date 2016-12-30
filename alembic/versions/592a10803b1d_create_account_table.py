"""create account table

Revision ID: 592a10803b1d
Revises:
Create Date: 2016-12-30 11:50:42.747150

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '592a10803b1d'
down_revision = '15f6f72bb848'
branch_labels = None
depends_on = None


def upgrade():
     op.create_table(
        'account',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200)),
    )


def downgrade():
    op.drop_table('account')

