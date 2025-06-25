from sqlalchemy import Column, Integer, String
from config import base


class User(base):
    __tablename__ = "users"

    id             = Column(Integer, primary_key=True, index=True)
    username       = Column(String(255), unique=True, nullable=True)
    email          = Column(String(255), unique=True, nullable=False)
    password       = Column(String(255), nullable=True)
    oauth_provider = Column(String(255), nullable=True)
    status         = Column(Integer, nullable=False)
