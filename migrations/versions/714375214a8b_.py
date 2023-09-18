"""empty message

Revision ID: 714375214a8b
Revises: 312b6c4ca7cf
Create Date: 2023-09-18 13:13:52.690916

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '714375214a8b'
down_revision = '312b6c4ca7cf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('burrito_orders', schema=None) as batch_op:
        batch_op.add_column(sa.Column('quantity', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('burrito_orders', schema=None) as batch_op:
        batch_op.drop_column('quantity')

    # ### end Alembic commands ###