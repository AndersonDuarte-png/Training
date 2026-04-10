from pydantic import BaseModel, field_validator
from typing import List


class Installments(BaseModel):
    month:int
    payment:float
    interest:float
    amortization:float
    remaining_balance:float

class LoanRequest(BaseModel):

    amount: float
    interest_rate: float
    months: int
    system: str


#comportamentos
    @field_validator("amount","interest_rate","months")
    @classmethod
    def validate_positive(cls,value):
        if value <= 0:
            raise ValueError("Apenas valores maior que zero")
        return value
    
    @field_validator("system")
    @classmethod
    def validate_LoanRequest_system(cls,value):
        if value != "PRICE" and value != "SAC":
            raise ValueError("Valor system incorreto")
        if value == "SAC":
            return value
        return value

    def genrate_installments(self) -> list[Installments]:
        if self.system == "SAC":
            return self.generate_sac_installments()
    
    def generate_sac_installments(self) ->list[Installments]:
        installments = []
        remaining_balance =  self.amount
        amortization = self.amount/self.months

        for N in range(1,self.months +1):
            interest = remaining_balance * self.interest_rate
            payment = amortization + interest
            remaining_balance -= amortization

            installments.append(
                Installments(
                    month=int(N),
                    amortization=round(amortization,2),
                    payment= round(payment,2),
                    interest = round(interest,2),
                    remaining_balance = round(remaining_balance,2)

            )
        )
        return installments
