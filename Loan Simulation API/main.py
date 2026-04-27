from fastapi import FastAPI
from models import LoanRequest,CompareRequest
from typing import List
from models import Installments
import services


app = FastAPI()


@app.post("/simulate")
def simulate_loan(request: LoanRequest):

    installments = request.genrate_installments()

    return{
        "monthly_payment":round(services.calculate_monthly_payment(request),2),
        "total_payment":round(services.calculate_total_payment(request,installments),2),
        "total_interest":round(services.calculate_total_interest(request,installments),2),
        "system":request.system,
        "Installments":installments
    }

@app.post("/compare")
def compare_loan(request: CompareRequest):
    price_total_interest = services.price_calculate_total_interest(request)
    price_total_payment = services.price_calculate_total_payment(request)
    installments = request.generate_sac_installments()
    sac_total_interest = services.sac_calculate_total_interest(installments)
    sac_total_payment = services.sac_calculate_total_payment(installments)
    savings_amount = services.calculate_savings_amount(sac_total_interest,price_total_interest)
    best_option = services.calculate_best_option(price_total_interest,sac_total_interest)
    
    return{
        "price_total_payment": round(price_total_payment,2),
        "price_total_interest": round(price_total_interest,2),
        "sac_total_payment": round(sac_total_payment,2),
        "sac_total_interest": round(sac_total_interest,2),
        "best_option":best_option,
        "savings_amount":round(savings_amount,2) 
    }


@app.get("/health")
def read_root():
    return {"status": "ok"}