from sqlalchemy import (
  create_engine,
  Column,
  UUID,
  Integer,
  String,
  DateTime,
  select,
  insert
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from datetime import datetime


Base = declarative_base()
engine = create_engine('sqlite:///products.db')
session = sessionmaker(bind=engine)()

class db_conn():
  def __init__(self) -> None:
    self.session = session

  def __enter__(self):
    return self.session.connection()

  def __exit__(self, exc_type, exc_value, exc_tb):
    self.session.close()


class Product(Base):
  # TODO: Add user 1-to-many relationship
  __tablename__ = 'product'
  id = Column(UUID, primary_key=True, autoincrement=False)
  created = Column(DateTime, default=datetime.now())
  name = Column(String)
  category = Column(String) # TODO: Add enums for categories
  price = Column(Integer)
  n_items_in_stock = Column(Integer)

# Create the tables in the engine
Base.metadata.create_all(engine)
