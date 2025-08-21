from sqlalchemy import Column, Integer, String, Float, Date
from .database import Base

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=False)   # instead of category/note
    amount = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
