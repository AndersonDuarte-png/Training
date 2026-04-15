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
    price_total_interest = round(services.price_calculate_total_interest(request),2)
    
    installments = request.generate_sac_installments()

    sac_total_interest = round(services.sac_calculate_total_interest(installments),2)
    
    return{
        "price_total_payment": round(services.price_calculate_total_payment(request),2),
        "price_total_interest": price_total_interest,
        "sac_total_payment": round(services.sac_calculate_total_payment(installments),2),
        "sac_total_interest": sac_total_interest,
        "best_option":services.calculate_best_option(price_total_interest,sac_total_interest)
    }


@app.get("/health")
def read_root():
    return {"status": "ok"}