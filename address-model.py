from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from db import engine


class Base(DeclarativeBase):
  pass


## Address Table
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