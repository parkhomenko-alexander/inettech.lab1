"""empty message

Revision ID: 57ff5ba7dc87
Revises: 6025379ed256
Create Date: 2021-10-29 00:53:30.926904

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '57ff5ba7dc87'
down_revision = '6025379ed256'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pas', sa.String(length=256), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'pas')
    # ### end Alembic commands ###
