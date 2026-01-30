# Product Category Matcher (Match-Case)
# Retail inventory management tool to categorize products for pricing strategies

# Prompt for product name, strip whitespace and lowercase
product_name = input("What's the product name? ").strip().lower()

# Use match-case to categorize products
match product_name:
    case "electronics" | "gadget":
        category = "High Margin"
    case product if product.startswith("tech"):
        category = "High Margin"
    case "clothing" | "apparel":
        category = "Medium Margin"
    case "food" | "grocery":
        category = "Low Margin"
    case _:
        category = "Uncategorized - Review Needed"

# Display result
print(f"Product: {product_name} | Category: {category}")
