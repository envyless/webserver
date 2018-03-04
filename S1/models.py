from sqlalchemy import Column, Integer, String
from database import Base

# mapping table class TbTest
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(30))
    password = Column(String(30))
    nickname = Column(String(250))
    money = Column(Integer, nullable=False)

