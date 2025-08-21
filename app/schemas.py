from pydantic import BaseModel
from datetime import date

class ExpenseCreate(BaseModel):
    description: str
    amount: float
    date: date

class ExpenseOut(ExpenseCreate):
    id: int

class Config:
    orm_mode = True