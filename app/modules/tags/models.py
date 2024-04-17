from datetime import datetime

from sqlalchemy import TIMESTAMP, Column, Integer, String
from app.database import Base


class Tag(Base):

    __tablename__ = "tags"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    name = Column(String, unique=True)
    description = Column(String)

    created_at = Column(TIMESTAMP, default=datetime.now)
    updated_at = Column(TIMESTAMP, default=datetime.now, onupdate=datetime.now)
