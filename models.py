from sqlalchemy import Column, String, Integer, Text, Boolean
from db import Base

class ToDo(Base):
    __tablename__="todos"

    id=Column(Integer, primary_key=True, index=True)
    Title= Column(String, index=True)
    desc=Column(Text)
    Status= Column(Boolean, index=True, default=False)