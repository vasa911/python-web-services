"""empty message

Revision ID: 8138ff1218ab
Revises: 27dced8ebee4
Create Date: 2020-07-25 17:18:58.410528

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8138ff1218ab'
down_revision = '27dced8ebee4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('author_id', sa.Integer(), nullable=True))
    op.create_foreign_key(op.f('fk_post_author_id_user'), 'post', 'user', ['author_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk_post_author_id_user'), 'post', type_='foreignkey')
    op.drop_column('post', 'author_id')
    # ### end Alembic commands ###
