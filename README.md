Development of an API that helps with financial calculation and normalization.

Adjust Inflation Route (POST) - Receives time series monetary values and update it by the inflation rate, currently just BRL available.

Inputs:
- Column/list of dates.
- Column/list of values.
- Date to adjust inflation rate.

Output:
- Dataframe: dates, original values, cumulative inflation (%), djusted values. 


Currency Rate Conversion Route (POST) - Receives time series monetary values (Dollar, Euro or Great Britain Pound) and convert it into the other 2 currencies.

Inputs:
- Column/list of dates.
- Column/list of values.
- Original currency as string.

Output:
- Dataframe: dates, value in Dollar, value in Euro, value in Great Britain Pound.
