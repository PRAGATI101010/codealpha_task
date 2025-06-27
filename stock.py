# Stock Portfolio Tracker

# Hardcoded stock prices (symbol: price per share)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2900,
    "AMZN": 3300
}

# User input for stock quantities
print("Enter your stock holdings:")
portfolio = {}

for stock in stock_prices:
    try:
        quantity = int(input(f"How many shares of {stock}? "))
        portfolio[stock] = quantity
    except ValueError:
        print("Invalid input. Setting quantity to 0.")
        portfolio[stock] = 0

# Calculate total investment
total_investment = 0
print("\nInvestment Summary:")
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    total_investment += investment
    print(f"{stock}: {quantity} shares x ₹{price} = ₹{investment}")

print(f"\nTotal Investment: ₹{total_investment}")

# Optionally, save the result to a .txt file
with open("portfolio_summary.txt", "w") as file:
    file.write("Investment Summary:\n")
    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        investment = price * quantity
        file.write(f"{stock}: {quantity} shares x ₹{price} = ₹{investment}\n")
    file.write(f"\nTotal Investment: ₹{total_investment}")

print("\nPortfolio summary saved to 'portfolio_summary.txt'")