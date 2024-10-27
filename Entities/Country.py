from sqlalchemy import Column, Integer, String
from db import Base

class Country(Base):
    __tablename__ = 'countries'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)