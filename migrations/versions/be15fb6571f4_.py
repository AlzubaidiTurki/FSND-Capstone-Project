"""empty message

Revision ID: be15fb6571f4
Revises: 7ec208412773
Create Date: 2021-09-02 23:37:26.759259

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be15fb6571f4'
down_revision = '7ec208412773'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('servant', 'isTaken')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('servant', sa.Column('isTaken', sa.BOOLEAN(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
