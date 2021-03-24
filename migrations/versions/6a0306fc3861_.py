"""empty message

Revision ID: 6a0306fc3861
Revises: 
Create Date: 2021-03-23 17:33:48.007369

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6a0306fc3861'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tblproperties',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=80), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('rooms', sa.String(length=3), nullable=True),
    sa.Column('bathrooms', sa.String(length=3), nullable=True),
    sa.Column('price', sa.String(length=100), nullable=True),
    sa.Column('proptype', sa.String(length=80), nullable=True),
    sa.Column('location', sa.String(length=255), nullable=True),
    sa.Column('photo', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tblproperties')
    # ### end Alembic commands ###
