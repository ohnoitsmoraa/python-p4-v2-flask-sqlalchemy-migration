"""rename address

Revision ID: dda90351c3c8
Revises: 05f9d4825141
Create Date: 2024-10-04 21:45:21.338503

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dda90351c3c8'
down_revision = '05f9d4825141'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('departments', sa.Column('location', sa.String(), nullable=True))
    op.drop_column('departments', 'address')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('departments', sa.Column('address', sa.VARCHAR(), nullable=True))
    op.drop_column('departments', 'location')
    # ### end Alembic commands ###
