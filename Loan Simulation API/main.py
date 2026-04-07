from fastapi import FastAPI
from models import LoanRequest


app = FastAPI()


@app.post("/simulate")
def simulate_loan(request: LoanRequest):
    return{
        "monthly_payment":round(request.monthly_payment(),2),
        "total_payment":round(request.calculateTotal_Payment(),2),
        "total_interest":round(request.calculateTotal_interest(),2),
    }

@app.get("/health")
def read_root():
    return {"status": "ok"}