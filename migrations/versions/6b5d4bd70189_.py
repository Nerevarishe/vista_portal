"""empty message

Revision ID: 6b5d4bd70189
Revises: 
Create Date: 2019-05-01 16:26:24.957632

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b5d4bd70189'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('defectura_card',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('drug_name', sa.String(), nullable=True),
    sa.Column('comment', sa.String(), nullable=True),
    sa.Column('employee_name', sa.String(), nullable=True),
    sa.Column('in_zd', sa.Boolean(), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('ip', sa.String(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_defectura_card_date'), 'defectura_card', ['date'], unique=False)
    op.create_index(op.f('ix_defectura_card_in_zd'), 'defectura_card', ['in_zd'], unique=False)
    op.create_table('drugstore_list',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ds_name', sa.String(), nullable=True),
    sa.Column('ds_adress', sa.String(), nullable=True),
    sa.Column('ds_worktime', sa.String(), nullable=True),
    sa.Column('ds_phone', sa.String(), nullable=True),
    sa.Column('ds_ip_phone', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('edinfo_post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('body', sa.String(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_edinfo_post_timestamp'), 'edinfo_post', ['timestamp'], unique=False)
    op.create_table('expdate_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('drug_name', sa.String(), nullable=True),
    sa.Column('exp_date', sa.DateTime(), nullable=True),
    sa.Column('amount', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_expdate_table_exp_date'), 'expdate_table', ['exp_date'], unique=False)
    op.create_table('faq_post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('body', sa.String(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_faq_post_timestamp'), 'faq_post', ['timestamp'], unique=False)
    op.create_table('law_post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('body', sa.String(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_law_post_timestamp'), 'law_post', ['timestamp'], unique=False)
    op.create_table('service_center_list',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('brands', sa.String(), nullable=True),
    sa.Column('sc_adress', sa.String(), nullable=True),
    sa.Column('sc_phone', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('shift',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('shift_name', sa.String(), nullable=True),
    sa.Column('comment', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sop_post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('body', sa.String(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_sop_post_timestamp'), 'sop_post', ['timestamp'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('employee',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('patronymic', sa.String(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('preferred_time', sa.String(), nullable=True),
    sa.Column('work_hours_in_day', sa.String(), nullable=True),
    sa.Column('shift', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['shift'], ['shift.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_employee_last_name'), 'employee', ['last_name'], unique=False)
    op.create_table('news',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(), nullable=True),
    sa.Column('source', sa.String(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_news_source'), 'news', ['source'], unique=False)
    op.create_index(op.f('ix_news_timestamp'), 'news', ['timestamp'], unique=False)
    op.create_table('schedule',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('year', sa.String(), nullable=True),
    sa.Column('month', sa.String(), nullable=True),
    sa.Column('employee_id', sa.Integer(), nullable=True),
    sa.Column('hours_in_month', sa.Integer(), nullable=True),
    sa.Column('vacation_days', sa.Integer(), nullable=True),
    sa.Column('vacation_start_date', sa.DateTime(), nullable=True),
    sa.Column('vacation_end_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['employee_id'], ['employee.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('schedule')
    op.drop_index(op.f('ix_news_timestamp'), table_name='news')
    op.drop_index(op.f('ix_news_source'), table_name='news')
    op.drop_table('news')
    op.drop_index(op.f('ix_employee_last_name'), table_name='employee')
    op.drop_table('employee')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_sop_post_timestamp'), table_name='sop_post')
    op.drop_table('sop_post')
    op.drop_table('shift')
    op.drop_table('service_center_list')
    op.drop_index(op.f('ix_law_post_timestamp'), table_name='law_post')
    op.drop_table('law_post')
    op.drop_index(op.f('ix_faq_post_timestamp'), table_name='faq_post')
    op.drop_table('faq_post')
    op.drop_index(op.f('ix_expdate_table_exp_date'), table_name='expdate_table')
    op.drop_table('expdate_table')
    op.drop_index(op.f('ix_edinfo_post_timestamp'), table_name='edinfo_post')
    op.drop_table('edinfo_post')
    op.drop_table('drugstore_list')
    op.drop_index(op.f('ix_defectura_card_in_zd'), table_name='defectura_card')
    op.drop_index(op.f('ix_defectura_card_date'), table_name='defectura_card')
    op.drop_table('defectura_card')
    # ### end Alembic commands ###
