"""create initial tables

Revision ID: 36539613eecf
Revises: 
Create Date: 2020-05-03 21:17:34.048638

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column
from flask_security.utils import encrypt_password


# revision identifiers, used by Alembic.
revision = '36539613eecf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'role',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.VARCHAR(80), nullable=False),
        sa.Column('description', sa.VARCHAR(255), nullable=True),
    )

    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('username', sa.VARCHAR(50), nullable=False),
        sa.Column('email', sa.VARCHAR(50), nullable=False),
        sa.Column('email_confirm', sa.TIMESTAMP, nullable=True),
        sa.Column('first_name', sa.VARCHAR(50), nullable=False),
        sa.Column('last_name', sa.VARCHAR(50), nullable=False),
        sa.Column('active', sa.Boolean, nullable=False),
        sa.Column('password', sa.VARCHAR(255), nullable=False),
    )
    user_table = table('user',
                       column('id'),
                       column('username'),
                       column('email'),
                       column('first_name'),
                       column('last_name'),
                       column('active'),
                       column('password'),
    )
    op.bulk_insert(user_table,
        [
            {'id': 1,
             'username': 'admin',
             'email': 'admin',
             'first_name': 'admin',
             'last_name': 'admin',
             'active': True,
             'password': encrypt_password('admin'),
             },

        ]
    )

    op.create_table(
        'user_roles',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('user_id', sa.Integer, nullable=False),
        sa.Column('role_id', sa.Integer, nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['user.id']),
        sa.ForeignKeyConstraint(['role_id'], ['role.id']),
    )

def downgrade():
    op.drop_table('role')
