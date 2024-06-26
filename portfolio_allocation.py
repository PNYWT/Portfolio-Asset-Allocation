# -*- coding: utf-8 -*-
"""Portfolio Allocation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1YY-t7YrWNabIIzodPeovOoq6G8VWsEBY
"""

import pandas as pd

# Define the function for future value calculation
def future_value_monthly_investment(principal, monthly_investment, annual_return_rate, months):
    monthly_return_rate = annual_return_rate / 12
    future_value = principal * (1 + monthly_return_rate) ** months
    future_value += monthly_investment * (((1 + monthly_return_rate) ** months - 1) / monthly_return_rate) * (1 + monthly_return_rate)
    return future_value

# Define the parameters for each investment
investment_params = {
    "USA S&P 500 ETF": {"monthly_investment_initial": 750, "annual_return_rate": 0.08, "monthly_investment_remaining": 1430.45},
    "USA NASDAQ 100 ETF": {"monthly_investment_initial": 750, "annual_return_rate": 0.10, "monthly_investment_remaining": 1430.45},
    "Europe ETF": {"monthly_investment_initial": 750, "annual_return_rate": 0.07, "monthly_investment_remaining": 1430.45},
    "China ETF": {"monthly_investment_initial": 750, "annual_return_rate": 0.09, "monthly_investment_remaining": 1430.45},
    "Asia ex Japan ETF": {"monthly_investment_initial": 1000, "annual_return_rate": 0.08, "monthly_investment_remaining": 1907.27},
    "Japan ETF": {"monthly_investment_initial": 1000, "annual_return_rate": 0.07, "monthly_investment_remaining": 1907.27},
}

# Define the investment periods
starting_age = 28
years_initial = 3
months_initial = years_initial * 12
years_remaining = 27 - years_initial
months_remaining = years_remaining * 12

# Calculate the future value for each month
data = []
total_future_value_carryover = {investment: 0 for investment in investment_params}

# Calculate future value for the initial period (1-3 years)
for month in range(1, months_initial + 1):
    age = starting_age + (month - 1) // 12
    entry = {"Year": (month - 1) // 12 + 1, "Month": (month - 1) % 12 + 1, "Age": age, "Total Future Value": 0}
    for investment, params in investment_params.items():
        future_value = future_value_monthly_investment(total_future_value_carryover[investment], params["monthly_investment_initial"], params["annual_return_rate"], 1)
        total_future_value_carryover[investment] = future_value
        entry[f"Future Value {investment}"] = future_value
        entry["Total Future Value"] += future_value
    data.append(entry)

# Calculate future value for the remaining period (4-27 years)
for month in range(1, months_remaining + 1):
    age = starting_age + years_initial + (month - 1) // 12
    entry = {"Year": (months_initial + month - 1) // 12 + 1, "Month": (months_initial + month - 1) % 12 + 1, "Age": age, "Total Future Value": 0}
    for investment, params in investment_params.items():
        future_value = future_value_monthly_investment(total_future_value_carryover[investment], params["monthly_investment_remaining"], params["annual_return_rate"], 1)
        total_future_value_carryover[investment] = future_value
        entry[f"Future Value {investment}"] = future_value
        entry["Total Future Value"] += future_value
    data.append(entry)

# Combine data into a DataFrame
df = pd.DataFrame(data)
df

# Calculate the total future value at the end of the period
total_future_value_end = df["Total Future Value"].iloc[-1]
total_future_value_end

# Save to Excel
#df.to_excel("updated_investment_plan_monthly_correct.xlsx")