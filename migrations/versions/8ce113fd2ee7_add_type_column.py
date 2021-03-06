"""Add type column

Revision ID: 8ce113fd2ee7
Revises: 0d6dbe4f92b5
Create Date: 2020-05-08 18:40:01.959118

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ce113fd2ee7'
down_revision = '0d6dbe4f92b5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('markers', sa.Column('marker_type', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('markers', 'marker_type')
    # ### end Alembic commands ###
