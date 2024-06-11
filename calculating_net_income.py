#This is my first project with Python

#defining earn amounts variables
bubblegum_earn = 202
toffee_earn = 118
icecream_earn = 2250
milk_choc_earn = 1680
doughnut_earn = 1075
pancake_earn = 80

#defining income variable
income = sum([bubblegum_earn, toffee_earn, icecream_earn, milk_choc_earn, doughnut_earn, pancake_earn])

#printing results
print("Earned amount:")
print(f"Bubblegum: ${bubblegum_earn}")
print(f"Toffee: ${toffee_earn}")
print(f"Ice cream: ${icecream_earn}")
print(f"Milk chocolate: ${milk_choc_earn}")
print(f"Doughnut: ${doughnut_earn}")
print(f"Pancake: ${pancake_earn}")
print(f"Income: ${income}")

#defining expenses variables
staff_expenses = float(input('What are your staff expenses?'))
other_expenses = float(input('What are your other expenses?'))

#defining net income variable
net_income = income - staff_expenses - other_expenses

#printing expenses and net income
print(f"Staff expenses: ${staff_expenses}")
print(f"Other expenses: ${other_expenses}")
print(f"Net income: ${net_income}")
