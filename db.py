from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#  db.py sy DATABASE connection bane ga
DATABASE_URL = "sqlite:///./sqlite.db"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)