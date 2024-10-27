from sqlalchemy import Column, Integer, String
from db import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
