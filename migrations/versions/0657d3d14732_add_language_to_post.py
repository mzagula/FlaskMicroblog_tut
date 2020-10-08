"""add language to post

Revision ID: 0657d3d14732
Revises: af146f2255b3
Create Date: 2020-10-08 21:18:12.751303

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0657d3d14732'
down_revision = 'af146f2255b3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'language')
    # ### end Alembic commands ###
