# from models import create_tables , drop_table
from users_models import create_table
from crud import create_user


create_table()
# drop_table()


# Users
create_user("Talha Rana", "example@gmail.com")