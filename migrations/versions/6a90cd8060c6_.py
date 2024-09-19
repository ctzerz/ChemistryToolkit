"""empty message

Revision ID: 6a90cd8060c6
Revises: 
Create Date: 2024-09-18 21:01:36.616908

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6a90cd8060c6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('element',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('elementName', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('element', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_element_elementName'), ['elementName'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('element', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_element_elementName'))

    op.drop_table('element')
    # ### end Alembic commands ###