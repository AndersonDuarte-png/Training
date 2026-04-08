from fastapi import FastAPI
from models import LoanRequest
import services


app = FastAPI()


@app.post("/simulate")
def simulate_loan(request: LoanRequest):
    return{
        "monthly_payment":round(services.calculate_monthly_payment(request),2),
        "total_payment":round(services.calculate_monthly_payment(request),2),
        "total_interest":round(services.calculate_total_payment(request),2),
        "system":request.system
    }

@app.get("/health")
def read_root():
    return {"status": "ok"}