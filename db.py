from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQL_DATABASE_URL= "postgresql://user:pass@localhost:5432/todolist"

engine=create_engine(SQL_DATABASE_URL)

session_local = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base=declarative_base()

def get_db():
    db= session_local()
    try:    
        yield db
    finally: 
        db.close()