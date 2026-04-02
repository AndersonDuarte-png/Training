from fastapi import FastAPI
from models import LoanRequest


app = FastAPI()


@app.post("/simulate")
def simulate_loan(request: LoanRequest):
    return request

@app.get("/health")
def read_root():
    return {"status": "ok"}