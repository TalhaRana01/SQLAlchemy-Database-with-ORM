from users_models import User, Post
from db import SessionLocal
from sqlalchemy import select, update

# Create User
def create_user(name: str, email:str):
  with SessionLocal() as session:
    user = User(name=name, email=email)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
  

## Method 1: Get All Users
# def get_all_users():
#   with SessionLocal() as session:
#     statement = select(User)
#     user = session.scalars(statement).all()
#     return user

# Method 2: Get All Users
# def get_all_users():
#   with SessionLocal() as session:
#     user = session.query(User).all()
#     return user

# Method 1: Get Single User by ID
# def get_user(user_id: int):
#   with SessionLocal() as session:
#     user = session.get_one(User, user_id)
#     return user


# Method 2: Get Single User by ID
# def get_user(user_id: int):
#   with SessionLocal() as session:
#     statement = select(User).where(User.id == user_id)
#     user = session.scalars(statement).one()
#     return user

# Update User with new email
def update_user_email(user_id:int, new_email:str):
  with SessionLocal() as session:
    user = session.get(User, user_id)
    if user:
      user.email = new_email
      session.commit()
      session.refresh(user)
    return user
  
## Method 1: Get Single Post by ID
# def get_post(post_id: int):
#   with SessionLocal() as session:
#     post = session.get_one(Post, post_id)
#     return post

## Method 2: Get Single Post by ID
# def get_post(post_id:int):
#   with SessionLocal() as session:
#     statement = select(Post).where(Post.id == post_id)
#     post = session.scalars(statement).one()
#     return post
    
  

# Create Post for a User
def create_post(user_id: int, title: str, content:str):
  with SessionLocal() as session:
    post = Post(user_id=user_id, title=title, content= content)
    session.add(post)
    session.commit()
    session.refresh(post)

## Method 1: Get All Posts
# def get_all_posts():
#   with SessionLocal() as session:
#     posts = session.query(Post).all()
#     return posts

## Method 2: Get All Posts
def get_all_posts():
  with SessionLocal() as session:
    posts = select(Post)
    return posts
    
## Method 1: Read all posts for an user
# def get_posts_by_user(user_id: int):
#   with SessionLocal() as session:
#     statement = select(Post).where(Post.user_id == user_id)
#     posts = session.scalars(statement).all()
#     return posts
  
  
## Method 1: Read all posts for an user
# def get_posts_by_user(user_id: int):
#   with SessionLocal() as session:
#     user = session.get(User, user_id)
#     posts = user.posts if user else []
#     return posts


# upddate post title
# def update_post_title(post_id: int, title: str):
#   with SessionLocal() as session:
#     post = session.get(Post, post_id)
#     if post:
#       post.title = title
#       session.commit()
#       session.refresh(post)
#     return post 
  

     

  