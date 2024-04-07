from sqlalchemy import Column, String, Boolean, Integer

from app.database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    password = Column(String)
    name = Column(String)
    is_active = Column(Boolean, default=True)
