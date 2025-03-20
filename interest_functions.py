def simple_interest(amount: float = None, principal: float = None, rate: float = None, time: int = None):

    if amount is None:
        amount = principal + (principal * rate * time)
        return amount
    
    elif principal is None:
        principal = (amount - principal) / (rate * time)
        return principal
    
    elif rate is None:
        rate = (amount - principal) / (principal * time)
        return rate
    
    elif time is None:
        time = (amount - principal) / (rate * principal)
        return time


def compound_interest(amount: float = None, principal: float = None, rate: float = None, time: int = None):
    
    import math

    if amount is None:
        amount = principal * ((1 + rate) ** time)
        return amount

    if principal is None:
        principal = amount / ((1 + rate) ** time)
        return principal

    if rate is None:
        rate = (amount / principal) ** (1 / time) - 1
        return rate

    if time is None:
        time = math.log(amount / principal) / math.log(1 + rate)
        return time
    

def present_value(future_value: float = None, projected_inflation_rate: float = None, time: float = None):

    present_value = future_value / ((1 + projected_inflation_rate) ** time)
    return present_value
