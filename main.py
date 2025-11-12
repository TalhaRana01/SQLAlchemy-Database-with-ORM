# from models import create_tables , drop_table
from users_models import create_table, delete_table
from crud import *

## Create Tables in Database
# create_table()
## Delete Tables from Database
# delete_table()

##----------------------
# Users
##----------------------


## Create User
# create_user("Nabeel", "example2@gmail.com")

## Get All Users
# print(get_all_users())

## Get Single User by ID
# print(get_user(2))

## Update User Email
# print(update_user_email(1, "mtalharana093@gmail.com"))

## Delete User
delete_user(1)

##----------------------
## Posts
##----------------------

## Create Post
# create_post(1, "First Post", "This is the content of the first post.")
# create_post(2, "Second Post", "This is the content of the second post.")
# create_post(3, "Third Post", "This is the content of the third post.")



## Get All Posts
# print(get_all_posts())


## Get single Post by ID
# print(get_post(1))


## Get post by User
# print(get_posts_by_user(1))
# print(get_posts_by_user(2))


## Update post title
# print(update_post_title(1, "method updated title"))

## Delete Post
delete_post(5)