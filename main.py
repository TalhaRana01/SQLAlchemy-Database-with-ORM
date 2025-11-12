# from models import create_tables , drop_table
from users_models import create_table, delete_table
from crud import create_user, create_post, get_user


## Create Tables in Database
# create_table()
## Delete Tables from Database
# delete_table()


# Users
# create_user("Talha Rana", "example@gmail.com")
print(get_user(1))

## Posts
# create_post(1, "First Post", "This is the content of the first post.")