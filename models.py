from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String
from db import engine


class Base(DeclarativeBase):
  pass

# User Model / user table

class User(Base):
  __tablename__ ="users"
  
  id: Mapped[int] = mapped_column(primary_key=True)
  name : Mapped[str] = mapped_column(String(50), nullable=False)
  email : Mapped[str] = mapped_column(String, nullable=False, unique=True)
  phone : Mapped[str] = mapped_column(String, nullable=False)
  
  
  def __repr__(self):
    return f"<User(id={self.id}, name={self.name}, email={self.email})>"
  
class Address(Base):
  __tablename__ ="address"
  
  id: Mapped[int] = mapped_column(primary_key=True)
  street : Mapped[str] = mapped_column(String(50), nullable=False)
  dist : Mapped[str] = mapped_column(String, nullable=False, unique=True)
  county : Mapped[str] = mapped_column(String, nullable=False, unique=True)
  
  
  def __repr__(self) -> str:
    return f"Address(id={self.id!r}, street={self.street!r})"
  
  

# Create Table
def create_tables():
  Base.metadata.create_all(engine)
  
# Delete Table
def drop_table():
  Base.metadata.drop_all(engine)