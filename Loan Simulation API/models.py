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
    
    def calculateTotal_interest(self):
         return float(self.calculateTotal_Payment() - self.amount)
    
    def calculateTotal_Payment(self):
        return float(self.monthly_payment()  * self.months)
    
    def monthly_payment(self):
        monthly_payment = self.amount * (self.interest_rate * (1 + self.interest_rate)**self.months) / ((1 + self.interest_rate)**self.months - 1)
        return monthly_payment