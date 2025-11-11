from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
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
  
  
  ## One to Many : User to Post
  # Relationshiop user to post
  posts: Mapped[list["Post"]] = relationship("Post", back_populates="user", cascade="all, delete")
  
  def __repr__(self)-> str:
    return f"<User(id={self.id}, name={self.name}, email={self.email})>"


## Post Model
class Post(Base):
  __tablename__ = "Post"
  
  id :Mapped[int] = mapped_column(primary_key=True)
  user_id : Mapped[int] = mapped_column(ForeignKey("user_id", ondelete="CASECADE"), nullable=False)
  title : Mapped[str] = mapped_column(String, nullable=False)
  content : Mapped[str] = mapped_column(String, nullable=False)
  
  # Relationship post to user
  user : Mapped["User"] = relationship("User", back_populates="posts")
  
  
  
  
  def __repr__(self) -> str:
    return f"<Post(id={self.id}, title={self.name})>"
  
  
  
## Address Table
# class Address(Base):
#   __tablename__ ="address"
  
#   id: Mapped[int] = mapped_column(primary_key=True)
#   street : Mapped[str] = mapped_column(String(50), nullable=False)
#   dist : Mapped[str] = mapped_column(String, nullable=False, unique=True)
#   county : Mapped[str] = mapped_column(String, nullable=False, unique=True)
  
  
#   def __repr__(self) -> str:
#     return f"Address(id={self.id!r}, street={self.street!r})"
  
  

# Create Table
def create_tables():
  Base.metadata.create_all(engine)
  
# Delete Table
def drop_table():
  Base.metadata.drop_all(engine)