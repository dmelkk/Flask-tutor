"""add permissions

Revision ID: 551efa3afbf
Revises: 2f889a6187c
Create Date: 2016-11-17 17:02:04.818116

"""

# revision identifiers, used by Alembic.
revision = '551efa3afbf'
down_revision = '2f889a6187c'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roles', sa.Column('default', sa.String(length=64), nullable=True))
    op.add_column('roles', sa.Column('permissions', sa.Integer(), nullable=True))
    op.create_index('ix_roles_default', 'roles', ['default'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_roles_default', 'roles')
    op.drop_column('roles', 'permissions')
    op.drop_column('roles', 'default')
    ### end Alembic commands ###
