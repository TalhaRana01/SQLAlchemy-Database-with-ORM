from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, ForeignKey
from db import engine


class Base(DeclarativeBase):
  pass 


# Create Table
def create_table():
  Base.metadata.create_all()
  
# Delete Table
def delete_table():
  Base.metadata.drop_all()