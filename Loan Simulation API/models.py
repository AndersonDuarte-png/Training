from pydantic import BaseModel, field_validator

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
