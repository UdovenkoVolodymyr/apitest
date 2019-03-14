"""empty message

Revision ID: 15964cd643c3
Revises: 
Create Date: 2019-03-14 16:52:22.126494

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15964cd643c3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('testdb',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('login', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('birthday', sa.String(), nullable=True),
    sa.Column('timestamp', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('testdb')
    # ### end Alembic commands ###
