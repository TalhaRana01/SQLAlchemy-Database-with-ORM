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

##----------------------
## Posts
##----------------------

## Create Post
# create_post(1, "First Post", "This is the content of the first post.")

## Get All Posts
print(get_all_posts())

## Get single Post by ID
# print(get_post(1))