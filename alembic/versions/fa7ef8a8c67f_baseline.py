"""baseline

Revision ID: fa7ef8a8c67f
Revises: cc8ada8f9d07
Create Date: 2017-01-02 14:02:27.705344

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa7ef8a8c67f'
down_revision = 'cc8ada8f9d07'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('root_cause', 'number')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('root_cause', sa.Column('number', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
