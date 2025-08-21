from sqlalchemy.orm import Session
from app import models, database, crud, schemas
from fastapi import FastAPI, Depends
from datetime import date

# Auto-create tables
models.Base.metadata.drop_all(bind=database.engine)   # wipes old tables
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Personal Expense Tracker")

# Dependency for DB
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/expenses", response_model=schemas.ExpenseOut)
def add_expense(payload: schemas.ExpenseCreate, db: Session = Depends(get_db)):
    return crud.create_expense(db, payload)

@app.get("/expenses", response_model=list[schemas.ExpenseOut])
def get_expenses(db: Session = Depends(get_db)):
    return crud.list_expenses(db)

@app.get("/summary")
def get_summary(for_date: str, db: Session = Depends(get_db)):
    total = crud.summary_by_date(db, for_date)
    return {
        "date": for_date,
        "total_spent": total
    }
