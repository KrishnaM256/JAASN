from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.schema import Table
from database import Base

class User(Base):
    __tablename__ = "users"
    __table_args__ = {"schema": "automation"}  # Define the schema explicitly

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)
