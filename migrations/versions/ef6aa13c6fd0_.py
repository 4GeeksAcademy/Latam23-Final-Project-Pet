"""empty message

Revision ID: ef6aa13c6fd0
Revises: e03974fdaae1
Create Date: 2024-02-05 23:56:18.807084

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef6aa13c6fd0'
down_revision = 'e03974fdaae1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('patient_file', schema=None) as batch_op:
        batch_op.add_column(sa.Column('veterinary_id', sa.Integer(), nullable=False))
        batch_op.drop_constraint('patient_file_veterinarian_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'veterinary', ['veterinary_id'], ['id'])
        batch_op.drop_column('veterinarian_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('patient_file', schema=None) as batch_op:
        batch_op.add_column(sa.Column('veterinarian_id', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('patient_file_veterinarian_id_fkey', 'veterinary', ['veterinarian_id'], ['id'])
        batch_op.drop_column('veterinary_id')

    # ### end Alembic commands ###
