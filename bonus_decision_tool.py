# Bonus: Business Decision Tool (Functions & Match-Case)
# Combined exercise: Evaluate business profitability and suggest investment strategies

def is_profitable(revenue, cost):
    """
    Helper function to check if a business is profitable.
    
    Args:
        revenue (float): Business revenue
        cost (float): Business cost
    
    Returns:
        bool: True if profitable (revenue > cost), False otherwise
    """
    return revenue > cost


def get_investment_suggestion(category):
    """
    Suggest investment strategy based on product category.
    
    Args:
        category (str): Product category
    
    Returns:
        str: Investment suggestion
    """
    match category:
        case "high margin":
            return "Reinvest in product development and marketing"
        case "medium margin":
            return "Expand distribution channels"
        case "low margin":
            return "Focus on volume and operational efficiency"
        case _:
            return "Review business model and market positioning"


def main():
    """
    Main function to prompt for business data and provide decision recommendations.
    """
    # Prompt for business inputs
    revenue = float(input("What's your business revenue? "))
    cost = float(input("What's your business cost? "))
    category = input("What's your product category? (high margin/medium margin/low margin) ").strip().lower()
    
    # Check profitability using helper function
    if is_profitable(revenue, cost):
        profit = revenue - cost
        suggestion = get_investment_suggestion(category)
        print(f"\nProfit: ${profit:,.2f}")
        print(f"Strategy: {suggestion}")
    else:
        loss = cost - revenue
        print(f"\nLoss: ${loss:,.2f}")
        print("Strategy: Reduce costs or pivot your business model")


# Run the main function
if __name__ == "__main__":
    main()
