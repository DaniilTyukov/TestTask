from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey, Float, create_engine, func, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
DATABASE_URL = 'postgresql://postgres:2197@db:5432/test'
engine = create_engine(
    DATABASE_URL
)

class Statistic(Base):
    __tablename__ = "statistics"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    x = Column(Float, nullable=False)
    y = Column(Float, nullable=False)
    z = Column(Float, nullable=False)
    device_id = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=False), default=func.now())
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="statistics")

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    statistics = relationship("Statistic", back_populates="user")

class UserCreate(BaseModel):
    name: str

class UserUpdate(BaseModel):
    name: str

class StatisticCreate(BaseModel):
    x: float
    y: float
    z: float
    device_id: int
    user_id: int

class StatisticUpdate(BaseModel):
    x: float
    y: float
    z: float
    device_id: int

Base.metadata.create_all(bind=engine)