#PROJECT-Stock Market Trading & Portfolio Simulator
import random
class Stock:
    def __init__(self, ticker, company_name, current_price):
        self.ticker = ticker.upper()
        self.company_name = company_name
        self.current_price = float(current_price)
        self.price_history = [self.current_price]

    def update_price(self, percentage_change):
        change_amount = self.current_price * (percentage_change / 100)
        self.current_price += change_amount
        self.price_history.append(round(self.current_price, 2))
        self.current_price = round(self.current_price, 2)


class Portfolio:
    def __init__(self):
        self.shares = {}
        self.buy_prices = {}

    def add_stock(self, ticker, qty, price):
        ticker = ticker.upper()
        if ticker in self.shares:
            total_cost = (self.shares[ticker] * self.buy_prices[ticker]) + (qty * price)
            self.shares[ticker] += qty
            self.buy_prices[ticker] = round(total_cost / self.shares[ticker], 2)
        else:
            self.shares[ticker] = qty
            self.buy_prices[ticker] = round(price, 2)

    def remove_stock(self, ticker, qty):
        ticker = ticker.upper()
        if ticker in self.shares and self.shares[ticker] >= qty:
            self.shares[ticker] -= qty
            if self.shares[ticker] == 0:
                del self.shares[ticker]
                del self.buy_prices[ticker]
            return True
        return False

    def calculate_value(self, market_stocks):
        total_value = 0.0
        for ticker, qty in self.shares.items():
            if ticker in market_stocks:
                total_value += qty * market_stocks[ticker].current_price
        return round(total_value, 2)


class User:
    def __init__(self, name, initial_balance):
        self.name = name
        self.initial_balance = float(initial_balance)
        self.portfolio = Portfolio()

    def buy(self, stock_obj, qty):
        if qty <= 0:
            print("Quantity must be greater than zero.")
            return False
        
        required_money = stock_obj.current_price * qty
        if self.initial_balance >= required_money:
            self.initial_balance -= required_money
            self.portfolio.add_stock(stock_obj.ticker, qty, stock_obj.current_price)
            print(f"Successfully bought {qty} shares of {stock_obj.ticker}.")
            return True
        else:
            print(f"Error: Insufficient funds. Required: ${round(required_money, 2)}, Available: ${round(self.initial_balance, 2)}")
            return False

    def sell(self, stock_obj, qty):
        ticker = stock_obj.ticker.upper()
        if ticker not in self.portfolio.shares or self.portfolio.shares[ticker] < qty:
            print(f"Error: You do not own enough shares of {ticker}.")
            return False
        if qty <= 0:
            print("Quantity must be greater than zero.")
            return False
        
        if self.portfolio.remove_stock(ticker, qty):
            earnings = stock_obj.current_price * qty
            self.initial_balance += earnings
            print(f"Successfully sold {qty} shares of {ticker} for ${round(earnings, 2)}.")
            return True
        return False

    def display_profile(self, market_stocks):
        print("\n==========================================")
        print(f"TRADER PROFILE: {self.name}")
        print(f"Wallet Balance: ${round(self.initial_balance, 2)}")
        portfolio_value = self.portfolio.calculate_value(market_stocks)
        print(f"Portfolio Value: ${portfolio_value}")
        print(f"Total Net Worth: ${round(self.initial_balance + portfolio_value, 2)}")
        print("---------------------------------------")
        print("Current Holdings:")
        if not self.portfolio.shares:
            print("  (No stocks in portfolio)")
        else:
            for ticker, qty in self.portfolio.shares.items():
                avg_p = self.portfolio.buy_prices[ticker]
                curr_p = market_stocks[ticker].current_price
                pnl = round((curr_p - avg_p) * qty, 2)
                pnl_str = f"+${pnl}" if pnl >= 0 else f"-${abs(pnl)}"
                print(f"  * {ticker}: {qty} Shares | Avg Price: ${avg_p} | Current Price: ${curr_p} | PnL: {pnl_str}")
        print("==========================================")


class MarketSimulator:
    def __init__(self):
        self.user = None
        self.all_stocks = {}

    def add_market_stock(self, stock_obj):
        self.all_stocks[stock_obj.ticker] = stock_obj

    def simulate_day(self):
        print("\nTrading Day End: Market Prices Fluctuate...")
        for stocks in self.all_stocks.values():
            percentage_change = random.uniform(-5.0, 5.0)
            stocks.update_price(percentage_change)
            print(f" * {stocks.ticker}: {round(percentage_change, 2)}% -> New Price: ${stocks.current_price}")

    def show_market(self):
        print("\nCURRENT MARKET PRICES")
        print("----------------------------------------------------")
        for stocks in self.all_stocks.values():
            print(f"Search: {stocks.ticker} ({stocks.company_name}) : ${stocks.current_price}")
        print("----------------------------------------------------")

    def start(self):
        print("--------------- Welcome to Stock Market Simulator -------------------")
        name = input("Enter your username: ")
        balance = float(input("Enter initial starting wallet balance: "))
        self.user = User(name, balance)

        self.add_market_stock(Stock("AAPL", "Apple Inc.", 150.0))
        self.add_market_stock(Stock("TSLA", "Tesla Motors", 250.0))
        self.add_market_stock(Stock("MSFT", "Microsoft Corp.", 320.0))
        self.add_market_stock(Stock("AMZN", "Amazon.com Inc.", 180.0))

        while True:
            print("\nMAIN MENU:")
            print("1. View Market Prices")
            print("2. Buy Stocks")
            print("3. Sell Stocks")
            print("4. View My Portfolio / Profile")
            print("5. End Day (Fluctuate Market)")
            print("6. Exit")

            choice = input("Select an option (1-6): ")
            if choice == "1":
                self.show_market()
            elif choice == "2":
                self.show_market()
                ticker = input("Enter Stock Ticker to Buy: ").upper()
                if ticker in self.all_stocks:
                    try:
                        qty = int(input(f"How many shares of {ticker}?: "))
                        self.user.buy(self.all_stocks[ticker], qty)
                    except ValueError:
                        print("Invalid quantity! Please enter a valid number.")
                else:
                    print("This stock ticker does not exist in the market!")
            elif choice == "3":
                if not self.user.portfolio.shares:
                    print("You do not own any stocks to sell!")
                    continue
                ticker = input("Enter Stock Ticker to Sell: ").upper()
                if ticker in self.all_stocks:
                    try:
                        qty = int(input(f"How many shares of {ticker} to sell?: "))
                        self.user.sell(self.all_stocks[ticker], qty)
                    except ValueError:
                        print("Invalid quantity!")
                else:
                    print("Invalid stock ticker!")
            elif choice == "4":
                self.user.display_profile(self.all_stocks)
            elif choice == "5":
                self.simulate_day()
            elif choice == "6":
                final_worth = self.user.initial_balance + self.user.portfolio.calculate_value(self.all_stocks)
                print(f"\nGoodbye {self.user.name}! Final Net Worth: ${round(final_worth, 2)}")
                break
            else:
                print("Invalid option, please select between 1-6.")


if __name__ == "__main__":
    sim = MarketSimulator()
    sim.start()
