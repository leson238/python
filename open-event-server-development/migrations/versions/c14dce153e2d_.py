"""empty message

Revision ID: c14dce153e2d
Revises: 3ea3ef8796a8
Create Date: 2016-07-22 09:28:56.773672

"""

# revision identifiers, used by Alembic.
revision = 'c14dce153e2d'
down_revision = '3ea3ef8796a8'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('versions', 'session_ver', new_column_name='sessions_ver')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('versions', 'sessions_ver', new_column_name='session_ver')
    ### end Alembic commands ###
