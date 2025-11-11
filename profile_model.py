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
  # posts: Mapped[list["Post"]] = relationship("Post", back_populates="user", cascade="all, delete")
  
  ## one-to-one User to profile
  profile : Mapped["Profile"] = relationship("Prfile", back_populates="user", uselist=False, cascade="all, delete")
  
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
  
  
  
#  Profile Model
class Profile(Base):
  __tablename__ = "profile"
  
  id :Mapped[int] = mapped_column(primary_key=True)
  user_id : Mapped[int] = mapped_column(ForeignKey("user_id", ondelete="CASECADE"), nullable=False, unique=True)
  bio : Mapped[str] = mapped_column(String, nullable=False)
  
  # Relationship profile to user
  user : Mapped["User"] = relationship("User", back_populates="profile")
  
  def __repr__(self) -> str:
  
    return f"<Post(id={self.id}, title={self.user_id})>"

# Address model
class Address(Base):
  __tablename__ = "address"
  
  id: Mapped[int] = mapped_column(primary_key=True)
  street : Mapped[str] = mapped_column(String, nullable=False)
  country : Mapped[str] = mapped_column(nullable=True, unique=True)
  
  
  user : Mapped[list[User]] = relationship("User", back_populates="address")
  
  def __repr__(self)-> str:
    return f"<Profile id={self.id} street={self.street} country={self.country} "
  
  
  
  
  
  
  

# Create Table
def create_tables():
  Base.metadata.create_all(engine)
  
# Delete Table
def drop_table():
  Base.metadata.drop_all(engine)