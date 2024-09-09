monthly_income = input('Enter your monthly income: ')
total_monthly_expenses = input('Enter your total monthly expenses: ')
annual_interest_rate = 0.05

monthly_income = int(monthly_income)
total_monthly_expenses = int(total_monthly_expenses)

monthly_savings = float(monthly_income - total_monthly_expenses)

projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)

print(f'Your monthly savings are ${monthly_savings}.')

print(f'Projected savings after one year, with interest, is: ${projected_savings}.')