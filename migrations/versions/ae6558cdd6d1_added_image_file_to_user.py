"""added image_file to User

Revision ID: ae6558cdd6d1
Revises: 320d5df33316
Create Date: 2020-05-22 20:41:34.323756

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae6558cdd6d1'
down_revision = '320d5df33316'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('image_file', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'image_file')
    # ### end Alembic commands ###
