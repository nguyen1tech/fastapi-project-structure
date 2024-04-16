from sqlalchemy import TIMESTAMP, Column, String, Integer

from app.database import Base


class Post(Base):

    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    author_id = Column(Integer)
    title = Column(String)
    content = Column(String)

    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)
