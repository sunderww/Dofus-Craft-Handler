"""empty message

Revision ID: d48b6aafcc1e
Revises: 80ecaaf9368a
Create Date: 2016-09-23 15:43:13.671210

"""

# revision identifiers, used by Alembic.
revision = 'd48b6aafcc1e'
down_revision = '80ecaaf9368a'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('item', sa.Column('lvl', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('item', 'lvl')
    ### end Alembic commands ###
