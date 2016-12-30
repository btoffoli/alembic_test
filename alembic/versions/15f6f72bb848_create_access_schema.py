"""create access schema

Revision ID: 15f6f72bb848
Revises: 592a10803b1d
Create Date: 2016-12-30 12:14:56.617981

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15f6f72bb848'
down_revision = None
branch_labels = None
depends_on = None

connection = op.get_bind()

def upgrade():
    connection.execute('CREATE SCHEMA access AUTHORIZATION postgres')
    connection.execute('GRANT ALL ON SCHEMA access TO postgres')
    connection.execute('GRANT ALL ON SCHEMA access TO public')
    connection.execute('COMMENT ON SCHEMA access IS \'standard public schema\';')

def downgrade():
    connection.execute('DROP SCHEMA access')
