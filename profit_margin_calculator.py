# Profit Margin Calculator (Variables & Basic Arithmetic)
# This program calculates the profit and profit margin based on user input for revenue and cost.    

# Prompt the user for revenue and cost
revenue = float(input("What's the revenue? "))
cost = float(input("What's the cost? "))

# Calculate profit
profit = revenue - cost

# Calculate margin and display results
if revenue > 0:
    margin = (profit / revenue) * 100
    print(f"Profit: ${profit:,.2f} | Margin: {margin:.2f}%")
else:
    print("Invalid revenue.")
