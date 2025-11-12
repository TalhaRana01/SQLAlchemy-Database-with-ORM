from users_models import User, Post
from db import SessionLocal
from sqlalchemy import select

# Create User
def create_user(name: str, email:str):
  with SessionLocal() as session:
    user = User(name=name, email=email)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

# Method 1: Read User by ID
# def get_user(user_id: int):
#   with SessionLocal() as session:
#     user = session.get_one(User, user_id)
#     return user


# Method 2: Read User by ID
def get_user(user_id: int):
  with SessionLocal() as session:
    statement = select(User).where(User.id == user_id)
    user = session.scalars(statement).one()
    return user
  
# # Read Post by ID
# def get_post(post_id: int):
#   with SessionLocal() as session:
#     post = session.get_one(Post, post_id)
#     return post

def get_post(post_id:int):
  with SessionLocal() as session:
    statement = select(Post).where(Post.id == post_id)
    post = session.scalars(statement).one()
    return post
    
  

# Create Post for a User
def create_post(user_id: int, title: str, content:str):
  with SessionLocal() as session:
    post = Post(user_id=user_id, title=title, content= content)
    session.add(post)
    session.commit()
    session.refresh(post)
    
  
  
  