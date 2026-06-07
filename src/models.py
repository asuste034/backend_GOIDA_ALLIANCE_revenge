from sqlalchemy import Column, Integer, String, String, JSON
from db import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False, index=True)

class EventBase(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    type = Column(String, index=True)
    block = Column(String, nullable=True, index=True)
    emergency_block = Column(String, nullable=True, index=True)