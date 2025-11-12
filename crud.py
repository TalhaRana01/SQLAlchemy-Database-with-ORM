from users_models import User, Post
from db import SessionLocal


# Create User
def create_user(name: str, email:str):
  with SessionLocal() as session:
    user = User(name=name, email=email)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

# Read User by ID
def get_user(user_id: int):
  with SessionLocal() as session:
    user = session.get_one(User, user_id)
    return user
  
# # Read User by ID
# def delete_user(user_id: int):
#   with SessionLocal() as session:
#     user = session.delete(User, user_id)
#     return user
    
  

# Create Post for a User
def create_post(user_id: int, title: str, content:str):
  with SessionLocal() as session:
    post = Post(user_id=user_id, title=title, content= content)
    session.add(post)
    session.commit()
    session.refresh(post)
    
  
  
  