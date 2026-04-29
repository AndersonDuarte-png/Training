#funcões
def calculate_monthly_payment(request):
    if request.system == "PRICE":
        return price_calculate_monthly_payment(request)
    elif request.system == "SAC":
        return sac__calculate_monthly_payment(request)

def calculate_total_payment(request,installments):
    if request.system == "PRICE":
        return price_calculate_total_payment(request)
    elif request.system == "SAC":
        return sac_calculate_total_payment(installments)

def calculate_total_interest(request,installments):
    if request.system == "PRICE":
        return price_calculate_total_interest(request)
    elif request.system == "SAC":
        return sac_calculate_total_interest(installments)


#pRICE FUNCTIONS
def price_calculate_total_interest(request):
        return float(price_calculate_total_payment(request) - request.amount)

def price_calculate_total_payment(request):
    return float(price_calculate_monthly_payment(request)  * request.months)

def price_calculate_monthly_payment(request):
    monthly_payment = request.amount * (request.interest_rate * (1 + request.interest_rate)**request.months) / ((1 + request.interest_rate)**request.months - 1)
    return monthly_payment

def calculate_savings_amount(sac_total_interest, price_total_interest):
    return abs(sac_total_interest - price_total_interest)



#SAC FUNCTIONS
def sac__calculate_monthly_payment(request):
    interest = request.amount * request.interest_rate
    amortization = request.amount / request.months
    return float(interest + amortization)

def sac_calculate_total_payment(installments):
    total = 0
    for n in installments:
        total+=n.payment
    return float(total)

def sac_calculate_total_interest(installments):
    total = 0
    for n in installments:
        total+=n.interest
    return float(total)


def calculate_best_option(price_interest,sac_interest):
    if price_interest < sac_interest:
        return "PRICE"
    elif price_interest > sac_interest:
        return "SAC"
    return "EQUAL"

def calculate_savings_percent(savings_amount, maior_total_interest):
    if savings_amount == maior_total_interest:
        return 0
    return (savings_amount/maior_total_interest)*100