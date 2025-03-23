# Development of an API that helps with financial calculation and normalization.

## Adjust Inflation Route (POST) - Receives time series monetary values and update it by the inflation rate, currently just BRL available.

Inputs:
- Column/list of dates.
- Column/list of values.
- Date to adjust inflation rate.

Output:
- Dataframe: dates, original values, cumulative inflation (%), djusted values. 


## Currency Rate Conversion Route (POST) - Receives time series monetary values (USD, Euro or Great Britain Pound) and convert it into the other 2 currencies.

Inputs:
- Column/list of dates.
- Column/list of values.
- Original currency as string.

Output:
- Dataframe: dates, value in USD, value in Euro, value in Great Britain Pound.

## French and SAC Amortization Calculation Route (POST) - Receives principal, interest rate and number of time periods and calculates its amortization process.

Inputs:
- Principal value.
- Interest rate.
- Number of time periods.

Output:
- Dataframe: period, payment, interest, principal, balance.

## Interest Calculation Route (POST) - Receives 3 values between total amount, principal, interest rate and number of time periods and calculates the missing one.

3 inputs between:
- Total amount value.
- Principal value.
- Interest rate.
- Number of time periods.

And the missing one as output.
