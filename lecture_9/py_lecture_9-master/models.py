from sqlalchemy import Boolean, Integer, Text, String, Column

from database import Base


class Item(Base):
    __table_args__ = {'extend_existing': True}
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    description = Column(Text)
    price = Column(Integer, nullable=False)
    on_offer = Column(Boolean, default=False)


class Users(Base):
    __table_args__ = {'extend_existing': True}
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
