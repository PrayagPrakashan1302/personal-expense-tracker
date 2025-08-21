# Personal Expense Tracker (FastAPI + SQLite)

A simple backend API to track daily expenses, built with **FastAPI**, **SQLite**, and **SQLAlchemy**.

---

## Features
- Add a new expense with description, amount, and date.
- List all expenses.
- Get a daily summary of total expenses for a given date.
- Built-in Swagger UI for easy testing.

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/personal-expense-tracker.git
   cd personal-expense-tracker
   ```

2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Running the app

Start the FastAPI server:
```bash
uvicorn app.main:app --reload
```

Open Swagger UI in your browser:
```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### Add an expense
**POST** `/expenses`
```json
{
  "description": "breakfast",
  "amount": 30,
  "date": "2025-08-21"
}
```

### Get all expenses
**GET** `/expenses`

### Get daily summary
**GET** `/summary?for_date=2025-08-21`
```json
{
  "date": "2025-08-21",
  "total_spent": 100
}
```

---

## Notes
- The database is stored in `app/expenses.db` (SQLite).
- For development, you can reset data by deleting the DB file:
  ```bash
  rm app/expenses.db
  ```

---

## License
MIT
