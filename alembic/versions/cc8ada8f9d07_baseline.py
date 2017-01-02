"""baseline

Revision ID: cc8ada8f9d07
Revises: 027cc30f39e4
Create Date: 2017-01-02 13:58:09.357660

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cc8ada8f9d07'
down_revision = '027cc30f39e4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('root_cause', sa.Column('number', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('root_cause', 'number')
    # ### end Alembic commands ###
