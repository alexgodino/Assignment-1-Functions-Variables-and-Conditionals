# Customer Greeting Formatter (Strings & Functions)
# Marketing tool to personalize customer greetings for improved engagement

def format_greeting(name, title="Customer"):
    """
    Format a personalized customer greeting.
    
    Args:
        name (str): Full name with possible whitespace
        title (str): Customer title (default: "Customer")
    
    Returns:
        str: Formatted greeting message
    """
    # strip() removes leading/trailing whitespace from the name
    cleaned_name = name.strip()
    
    # Handle empty name
    if not cleaned_name:
        return "Hello, Valued Customer!"
    
    # title() capitalizes the first letter of each word
    titled_name = cleaned_name.title()
    
    # split() divides the string into words, get first element [0]
    first_name = titled_name.split()[0]
    
    # Return formatted greeting with title
    return f"Hello, {first_name} ({title})!"

# Main code
full_name = input("What's your full name? ")
greeting = format_greeting(full_name)
print(greeting)
