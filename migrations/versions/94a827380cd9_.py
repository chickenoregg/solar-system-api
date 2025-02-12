"""empty message

Revision ID: 94a827380cd9
Revises: 718239a6e2f1
Create Date: 2023-05-08 18:01:36.179441

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '94a827380cd9'
down_revision = '718239a6e2f1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('moon',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('planet_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['planet_id'], ['planet.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('moon')
    # ### end Alembic commands ###
