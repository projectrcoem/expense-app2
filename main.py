from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Expense(BaseModel):
    name: str
    amount: float

@app.post("/expenses/", response_model=List[Expense])
def create_expenses(expenses: List[Expense]):
    return expenses

@app.get("/expenses/", response_model=List[Expense])
def read_expenses():
    return [
        {"name": "Groceries", "amount": 50.0},
        {"name": "Rent", "amount": 1000.0},
        {"name": "Utilities", "amount": 200.0},
    ]
