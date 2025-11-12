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
  
  
  