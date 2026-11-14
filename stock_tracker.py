def stock_tracker():
    # Hardcoded stock prices
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 140,
        "AMZN": 175,
        "MSFT": 420
    }
    
    portfolio = {}
    total_investment = 0
    
    print("Available Stocks:", ", ".join(stock_prices.keys()))
    print("Enter 'done' when finished.\n")
    
    while True:
        stock = input("Enter stock symbol (e.g., AAPL): ").strip().upper()
        if stock == "DONE":
            break
        if stock not in stock_prices:
            print("Stock not found. Please choose from the available list.\n")
            continue
            
        try:
            quantity = int(input(f"Enter quantity for {stock}: "))
            if quantity <= 0:
                print("Quantity must be greater than 0.\n")
                continue
        except ValueError:
            print("Please enter a valid number.\n")
            continue
            
        portfolio[stock] = portfolio.get(stock, 0) + quantity
        total_investment += stock_prices[stock] * quantity
        print(f"Added {quantity} shares of {stock}.\n")
        
    print("\n--- Portfolio Summary ---")
    for stock, qty in portfolio.items():
        value = stock_prices[stock] * qty
        print(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${value}")
    print(f"Total Investment Value: ${total_investment}")
    
    # Optional: Save result to a .txt file
    save = input("\nDo you want to save this summary to a file? (yes/no): ").strip().lower()
    if save == "yes":
        with open("portfolio_summary.txt", "w") as file:
            file.write("--- Portfolio Summary ---\n")
            for stock, qty in portfolio.items():
                value = stock_prices[stock] * qty
                file.write(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${value}\n")
            file.write(f"Total Investment Value: ${total_investment}\n")
        print("Saved to 'portfolio_summary.txt'!")

if __name__ == "__main__":
    stock_tracker()