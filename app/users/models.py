from sqlalchemy import Column, String, Boolean, Integer

from app.database import Base


class User(Base):

    __tablename__ = "users"
    __table_args__ = {'schema' : 'fastapi_example'}

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    password = Column(String)
    name = Column(String)
    is_active = Column(Boolean, default=True)
