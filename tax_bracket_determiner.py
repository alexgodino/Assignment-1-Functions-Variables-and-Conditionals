# Tax Bracket Determiner (Conditionals & Functions Returning Values)
# Tax consulting tool to determine employee income tax bracket for deduction advice

def get_tax_bracket(income):
    """
    Determine tax bracket based on annual income.
    
    Args:
        income (float): Annual income
    
    Returns:
        tuple: (bracket_str, rate) or (error_msg, 0) if invalid
    """
    # Validate income
    if income < 0:
        return "Invalid income.", 0
    
    # Use if/elif to determine bracket and rate
    if income < 50000:
        bracket = "Low (10%)"
        rate = 0.10
    elif income < 100000:
        bracket = "Medium (20%)"
        rate = 0.20
    else:
        bracket = "High (30%)"
        rate = 0.30
    
    # Ternary: Check if income is even for deduction eligibility
    bracket = bracket + " (Deduction Eligible)" if income % 2 == 0 else bracket
    
    return bracket, rate


# Main code
income = float(input("What's your annual income? "))
bracket, rate = get_tax_bracket(income)

# Calculate and display results
if rate > 0:  # Valid income
    estimated_tax = income * rate
    print(f"Your bracket: {bracket}. Estimated tax: {estimated_tax}")
else:
    print(f"Your bracket: {bracket}.")
