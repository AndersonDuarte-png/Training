
#funcões

def calculate_monthly_payment(request):
    if request.system == "PRICE":
        return price_calculate_monthly_payment(request)
    elif request.system == "SAC":
        return sac__calculate_monthly_payment(request)

def calculate_total_payment(request):
    if request.system == "PRICE":
        return price_calculate_total_payment(request)
    elif request.system == "SAC":
        return sac_calculate_total_payment(request)

def calculate_total_interest(request):
    if request.system == "PRICE":
        return price_calculate_total_interest(request)
    elif request.system == "SAC":
        return sac_calculate_total_interest(request)


#pRICE FUNCTIONS
def price_calculate_total_interest(request):
        return float(price_calculate_total_payment(request) - request.amount)

def price_calculate_total_payment(request):
    return float(price_calculate_monthly_payment(request)  * request.months)

def price_calculate_monthly_payment(request):
    monthly_payment = request.amount * (request.interest_rate * (1 + request.interest_rate)**request.months) / ((1 + request.interest_rate)**request.months - 1)
    return monthly_payment

#SAC FUNCTIONS
def sac__calculate_monthly_payment(request):
    interest = request.amount * request.interest_rate
    amortization = request.amount / request.months
    return float(interest + amortization)

def sac_calculate_total_payment(request):
    return float(request.amount + sac_calculate_total_interest(request))

def sac_calculate_total_interest(request):
    return float(request.interest_rate * request.amount * (request.months + 1) / 2)