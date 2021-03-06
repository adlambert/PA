"""Feedback table

Revision ID: d3ce4408bc0d
Revises: 8ce113fd2ee7
Create Date: 2020-06-24 19:32:39.739748

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd3ce4408bc0d'
down_revision = '8ce113fd2ee7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('feedback',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('item', sa.String(length=32), nullable=True),
    sa.Column('fname', sa.String(length=32), nullable=True),
    sa.Column('contact', sa.String(length=32), nullable=True),
    sa.Column('copyright', sa.Boolean(), nullable=True),
    sa.Column('privacy', sa.Boolean(), nullable=True),
    sa.Column('message', sa.UnicodeText(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_feedback_timestamp'), 'feedback', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_feedback_timestamp'), table_name='feedback')
    op.drop_table('feedback')
    # ### end Alembic commands ###
