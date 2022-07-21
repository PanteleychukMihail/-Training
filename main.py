from datetime import datetime

from sqlalchemy import (
   create_engine,
   MetaData,
   Table,
   Integer,
   String,
   Column,
   DateTime,
   ForeignKey,
   Numeric,
   CheckConstraint
)
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import psycopg2

connection = psycopg2.connect(user="postgres", password="sdzxSDZX")
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

cursor = connection.cursor()
sql_create_database = cursor.execute('create database sqlalchemy_rest1')

cursor.close()
connection.close()

metadata = MetaData()
engine = create_engine("postgresql+psycopg2://postgres:sdzxSDZX@localhost/sqlalchemy_rest1", echo=True)

customers = Table('customers', metadata,
    Column('id', Integer(), primary_key=True),
    Column('first_name', String(100), nullable=False),
    Column('last_name', String(100), nullable=False),
    Column('username', String(50), nullable=False),
    Column('email', String(200), nullable=False),
    Column('address', String(200), nullable=False),
    Column('town', String(50), nullable=False),
    Column('created_on', DateTime(), default=datetime.now),
    Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)
)

items = Table('items', metadata,
    Column('id', Integer(), primary_key=True),
    Column('name', String(200), nullable=False),
    Column('cost_price', Numeric(10, 2), nullable=False),
    Column('selling_price', Numeric(10, 2),  nullable=False),
    Column('quantity', Integer(), nullable=False),
    CheckConstraint('quantity > 0', name='quantity_check')
)


orders = Table('orders', metadata,
    Column('id', Integer(), primary_key=True),
    Column('customer_id', ForeignKey('customers.id')),
    Column('date_placed', DateTime(), default=datetime.now),
    Column('date_shipped', DateTime())
)


order_lines = Table(
    'order_lines',
    metadata,
    Column('id', Integer(), primary_key=True),
    Column('order_id', ForeignKey('orders.id')),
    Column('item_id', ForeignKey('items.id')),
    Column('quantity', Integer())
)

students = Table(
   'students', metadata,
   Column('id', Integer, primary_key = True),
   Column('name', String),
   Column('lastname', String),
)
metadata.create_all(engine)

for t in metadata.tables:
    print(metadata.tables[t])

print('-------------')

for t in metadata.sorted_tables:
    print(t.name)
