class Account:
    def __init__(self, user_id: str, initial_deposit: float):
        self.user_id = user_id
        self.initial_deposit = initial_deposit
        self.balance = initial_deposit
        self.holdings = {}
        self.transactions = []

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount: float) -> bool:
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            return True
        return False

    def buy_shares(self, symbol: str, quantity: int) -> bool:
        if quantity > 0:
            price = self.get_share_price(symbol)
            total_cost = price * quantity
            if self.balance >= total_cost:
                self.balance -= total_cost
                self.holdings[symbol] = self.holdings.get(symbol, 0) + quantity
                self.transactions.append({'action': 'buy', 'symbol': symbol, 'quantity': quantity, 'price': price})
                return True
        return False

    def sell_shares(self, symbol: str, quantity: int) -> bool:
        if quantity > 0 and self.holdings.get(symbol, 0) >= quantity:
            price = self.get_share_price(symbol)
            total_sale = price * quantity
            self.balance += total_sale
            self.holdings[symbol] -= quantity
            if self.holdings[symbol] == 0:
                del self.holdings[symbol]
            self.transactions.append({'action': 'sell', 'symbol': symbol, 'quantity': quantity, 'price': price})
            return True
        return False

    def calculate_portfolio_value(self) -> float:
        total_value = self.balance
        for symbol, quantity in self.holdings.items():
            total_value += self.get_share_price(symbol) * quantity
        return total_value

    def calculate_profit_loss(self) -> float:
        current_value = self.calculate_portfolio_value()
        return current_value - self.initial_deposit

    def report_holdings(self) -> dict:
        return self.holdings.copy()

    def report_transactions(self) -> list:
        return self.transactions.copy()

    def get_share_price(self, symbol: str) -> float:
        # Test implementation
        share_prices = {'AAPL': 150.0, 'TSLA': 700.0, 'GOOGL': 2800.0}
        return share_prices.get(symbol, 0.0)
