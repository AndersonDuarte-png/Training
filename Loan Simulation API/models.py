from pydantic import BaseModel, field_validator

class LoanRequest(BaseModel):

    amount: float
    interest_rate: float
    months: int

    @field_validator("amount","interest_rate","months")
    @classmethod
    def validate_positive(cls,value):
        if value <= 0:
                raise ValueError("Apenas valores maior que zero")
        return value