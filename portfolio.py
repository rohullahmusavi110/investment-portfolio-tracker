import csv

portfolio = {}

number_of_stocks = int(input("How many stocks do you want to add? "))

for i in range(number_of_stocks):
    print(f"\nEnter details for stock {i + 1}")

    ticker = input("Enter stock ticker: ").upper()
    buy_price = float(input("Enter buy price: "))
    quantity = int(input("Enter number of shares: "))
    current_price = float(input("Enter current stock price: "))

    portfolio[ticker] = {
        "buy_price": buy_price,
        "quantity": quantity,
        "current_price": current_price
    }

total_invested = 0
total_market_value = 0

with open("portfolio_summary.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Ticker", "Buy Price", "Quantity",
        "Current Price", "Invested Amount",
        "Market Value", "Profit/Loss",
        "Gain/Loss Percentage"
    ])

    for ticker, details in portfolio.items():
        buy_price = details["buy_price"]
        quantity = details["quantity"]
        current_price = details["current_price"]

        invested = buy_price * quantity
        market_value = current_price * quantity
        profit_loss = market_value - invested

        percentage = (
            (profit_loss / invested) * 100
            if invested != 0 else 0
        )

        total_invested += invested
        total_market_value += market_value

        print(f"\nTicker: {ticker}")
        print(f"Invested: ${invested:.2f}")
        print(f"Market Value: ${market_value:.2f}")
        print(f"Profit/Loss: ${profit_loss:.2f}")
        print(f"Gain/Loss Percentage: {percentage:.2f}%")

        writer.writerow([
            ticker, buy_price, quantity, current_price,
            invested, market_value, profit_loss, percentage
        ])

    total_profit_loss = total_market_value - total_invested

    total_percentage = (
        (total_profit_loss / total_invested) * 100
        if total_invested != 0 else 0
    )

    writer.writerow([])
    writer.writerow([
        "TOTAL", "", "", "",
        total_invested, total_market_value,
        total_profit_loss, total_percentage
    ])

print("\n--- Portfolio Summary ---")
print(f"Total Invested: ${total_invested:.2f}")
print(f"Total Market Value: ${total_market_value:.2f}")
print(f"Total Profit/Loss: ${total_profit_loss:.2f}")
print(f"Total Gain/Loss Percentage: {total_percentage:.2f}%")
print("\nCSV report saved successfully!")
