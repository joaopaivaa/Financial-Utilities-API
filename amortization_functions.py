def french_amortization(principal, rate, periods):
    
    import pandas as pd 

    # Calculate the fixed installment (PMT)
    payment = principal * rate / (1 - (1 + rate) ** -periods)
    balance = principal

    df = pd.DataFrame(columns=['Period','Payment','Interest','Principal','Balance'])
    new_line = pd.DataFrame({'Period': [0],
                         'Payment': [''],
                         'Interest': [''],
                         'Principal': [''],
                         'Balance': ['']})
    df = pd.concat([df, new_line], ignore_index=True)

    for period in range(1, periods + 1):
        interest = balance * rate
        principal_payment = payment - interest
        balance -= principal_payment
        new_line = pd.DataFrame({'Period': [round(period, 2)],
                                 'Payment': [round(payment, 2)],
                                 'Interest': [round(interest, 2)],
                                 'Principal': [round(principal_payment, 2)],
                                 'Balance': [round(balance, 2)]})
        df = pd.concat([df, new_line], ignore_index=True)
    
    return df


def sac_amortization(principal, rate, periods):

    import pandas as pd

    # Calculate constant amortization
    amortization = principal / periods
    balance = principal

    df = pd.DataFrame(columns=['Period','Payment','Interest','Principal','Balance'])
    new_line = pd.DataFrame({'Period': [0],
                         'Payment': [''],
                         'Interest': [''],
                         'Principal': [''],
                         'Balance': ['']})
    df = pd.concat([df, new_line], ignore_index=True)

    for period in range(1, periods + 1):
        interest = balance * rate
        payment = amortization + interest
        balance -= amortization
        new_line = pd.DataFrame({'Period': [round(period, 2)],
                                 'Payment': [round(payment, 2)],
                                 'Interest': [round(interest, 2)],
                                 'Principal': [round(amortization, 2)],
                                 'Balance': [round(balance, 2)]})
        df = pd.concat([df, new_line], ignore_index=True)

    return df
