"""is_need_review column to Attempts table

Revision ID: 320d5df33316
Revises: bcbea71ebf2a
Create Date: 2020-05-16 19:14:09.770901

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '320d5df33316'
down_revision = 'bcbea71ebf2a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('attempts', sa.Column('is_needs_review', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('attempts', 'is_needs_review')
    # ### end Alembic commands ###