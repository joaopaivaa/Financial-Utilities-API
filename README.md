# Financial Utilities API

Author: João Paiva.

Contact: joaopaiva.datascience@gmail.com

Github: https://github.com/joaopaivaa

Portfolio: https://joaopaivaa.github.io/

## :money_with_wings: Inflation Adjustment Route (POST)

Receives time series monetary values and adjusts it by the CPI rate.

Available for:
- BRL;
- GBP;
- USD.

Inputs:
- List of dates.
- List of nominal values.
- Adjustment reference date.

Output:
- Dataframe: dates, nominal values, accumulated inflation (%), adjusted/real values. 

## :dollar: Currency Rate Conversion Route (POST)

Receives time series monetary values and converts it into other currencies.

Available for:
- Euro to GBP;
- Euro to USD;
- GBP to Euro;
- GBP to USD;
- USD to Euro;
- USD to GBP.

Inputs:
- List of dates.
- List of values.
- Original currency as string.

Output:
- Dataframe: dates, value in USD, value in Euro, value in Great Britain Pound.

## :chart_with_downwards_trend: French Amortization Calculation Route (POST)

Receives principal, interest rate and number of time periods and calculates its amortization process.

Inputs:
- Principal value.
- Interest rate.
- Number of time periods.

Output:
- Dataframe: period, payment, interest, principal, balance.

## :chart_with_downwards_trend: SAC Amortization Calculation Route (POST)

Receives principal, interest rate and number of time periods and calculates its amortization process.

Inputs:
- Principal value.
- Interest rate.
- Number of time periods.

Output:
- Dataframe: period, payment, interest, principal, balance.

## :chart_with_upwards_trend: Simple Interest Route (POST)

Receives 3 values between total amount, principal, interest rate and number of time periods and calculates the missing one.

3 inputs between:
- Total amount value.
- Principal value.
- Interest rate.
- Number of time periods.

And the missing one as output.

## :chart_with_upwards_trend: Compound Interest Route (POST)

Receives 3 values between total amount, principal, interest rate and number of time periods and calculates the missing one.

3 inputs between:
- Total amount value.
- Principal value.
- Interest rate.
- Number of time periods.

And the missing one as output.

## :link Access the API

Link to the API: https://financial-utilities-api.onrender.com/docs
