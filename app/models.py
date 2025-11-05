from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    role = Column(String)  # volunteer, corporate, admin, ngo
    created_at = Column(DateTime, default=func.now())

class Matching(Base):
    __tablename__ = "matches"
    id = Column(Integer, primary_key=True)
    volunteer_id = Column(Integer, ForeignKey("users.id"))
    ngo_id = Column(Integer, ForeignKey("users.id"))
    status = Column(String)  # matched, pending, rejected
    created_at = Column(DateTime, default=func.now())
