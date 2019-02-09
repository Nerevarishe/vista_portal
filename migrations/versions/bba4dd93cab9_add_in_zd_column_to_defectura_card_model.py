"""add in_zd column to defectura card model

Revision ID: bba4dd93cab9
Revises: 89397475a201
Create Date: 2019-02-09 11:50:20.723008

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bba4dd93cab9'
down_revision = '89397475a201'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('defectura_card', sa.Column('in_zd', sa.Boolean(), nullable=True))
    op.create_index(op.f('ix_defectura_card_in_zd'), 'defectura_card', ['in_zd'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_defectura_card_in_zd'), table_name='defectura_card')
    op.drop_column('defectura_card', 'in_zd')
    # ### end Alembic commands ###
