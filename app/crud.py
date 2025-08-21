from sqlalchemy.orm import Session
from sqlalchemy import func
from app import models, schemas

def create_expense(db: Session, payload: schemas.ExpenseCreate):
    exp = models.Expense(
        description=payload.description,
        amount=payload.amount,
        date=payload.date,
    )
    db.add(exp)
    db.commit()
    db.refresh(exp)
    return exp

def list_expenses(db: Session):
    return db.query(models.Expense).all()

def summary_by_date(db: Session, date):
    result = (
        db.query(func.sum(models.Expense.amount))
        .filter(models.Expense.date == date)   # only this date
        .scalar()
    )
    return result or 0
