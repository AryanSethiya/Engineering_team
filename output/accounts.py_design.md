# accounts.py Design

This module will contain an `Account` class that manages user account activities within a trading simulation platform. The class contains various methods to conduct transactions, calculate portfolio values, and manage user holdings. Below is the detailed design of the class and methods:

## Class: `Account`

### Attributes
- `user_id`: A unique identifier for each account holder.
- `balance`: The current balance of cash in the account.
- `holdings`: A dictionary mapping of stock symbols to quantities owned.
- `transactions`: A list of transaction records detailing each buy/sell action.
- `initial_deposit`: The initial amount of cash deposited.

### Methods

#### `__init__(self, user_id: str, initial_deposit: float)`
Constructor to initialize an account.
- **Parameters**:
  - `user_id` (str): The user's unique identifier.
  - `initial_deposit` (float): The amount of initial deposit.
- **Functionality**: Sets up the account with the initial deposit, initializes balance, holdings, and transactions.

#### `deposit(self, amount: float) -> None`
Deposit funds into the account.
- **Parameters**:
  - `amount` (float): The amount to deposit.
- **Functionality**: Increases the account balance by the deposit amount.

#### `withdraw(self, amount: float) -> bool`
Withdraw funds from the account.
- **Parameters**:
  - `amount` (float): The amount to withdraw.
- **Functionality**: Decreases the account balance by the withdraw amount if sufficient funds are available.
- **Returns**: `True` if the withdrawal was successful, `False` otherwise.

#### `buy_shares(self, symbol: str, quantity: int) -> bool`
Buy a specified number of shares.
- **Parameters**:
  - `symbol` (str): The ticker symbol of the shares to buy.
  - `quantity` (int): The number of shares to buy.
- **Functionality**: Checks if enough funds are available; if so, deducts the total price from balance, increases holdings, and records the transaction.
- **Returns**: `True` if the purchase was successful, `False` otherwise.

#### `sell_shares(self, symbol: str, quantity: int) -> bool`
Sell a specified number of shares.
- **Parameters**:
  - `symbol` (str): The ticker symbol of the shares to sell.
  - `quantity` (int): The number of shares to sell.
- **Functionality**: Checks if enough shares are available; if so, increases the balance by the total sale price, decreases holdings, and records the transaction.
- **Returns**: `True` if the sale was successful, `False` otherwise.

#### `calculate_portfolio_value(self) -> float`
Calculate the total value of the user's portfolio.
- **Returns**: The sum of the cash balance and market value of all shares held.

#### `calculate_profit_loss(self) -> float`
Calculate the profit or loss based on initial deposit.
- **Returns**: The net profit or loss figure as balance + current portfolio value – initial deposit.

#### `report_holdings(self) -> dict`
Return a summary of current holdings.
- **Returns**: A dictionary mapping symbols to quantities of shares held.

#### `report_transactions(self) -> list`
List all transactions made by the user.
- **Returns**: A list of dictionaries, with each transaction's details.

#### `get_share_price(self, symbol: str) -> float`
Retrieve the current price of a specific share.
- **Parameters**:
  - `symbol` (str): The ticker symbol for which to get the price.
- **Functionality**: Calls the provided `get_share_price(symbol)` function to obtain the share price.
- **Returns**: The current share price for the given symbol.

---

Ensure to handle exceptions and invalid operations such as insufficient balance or invalid symbols within each method to maintain robustness in the module.