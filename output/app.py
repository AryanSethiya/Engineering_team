import gradio as gr
from accounts import Account

# Initialize the account with a demo user and initial deposit of $1000
default_initial_deposit = 1000.0
account = Account(user_id="demo_user", initial_deposit=default_initial_deposit)

def dispatch_action(action, initial_deposit, amount, symbol, quantity):
    global account
    if action == "Create Account":
        account = Account(user_id="demo_user", initial_deposit=initial_deposit)
        return f"Account created with an initial deposit of ${initial_deposit}. Current balance: ${account.balance}", account.balance, account.holdings, account.transactions
    elif action == "Deposit":
        account.deposit(amount)
        return f"Deposited ${amount}. Current balance: ${account.balance}", account.balance, account.holdings, account.transactions
    elif action == "Withdraw":
        success = account.withdraw(amount)
        if success:
            return f"Withdrew ${amount}. Current balance: ${account.balance}", account.balance, account.holdings, account.transactions
        else:
            return "Withdrawal failed. Insufficient funds or invalid amount.", account.balance, account.holdings, account.transactions
    elif action == "Buy Shares":
        success = account.buy_shares(symbol, quantity)
        if success:
            return f"Bought {quantity} shares of {symbol}. Current balance: ${account.balance}", account.balance, account.holdings, account.transactions
        else:
            return "Purchase failed. Insufficient funds or invalid transaction.", account.balance, account.holdings, account.transactions
    elif action == "Sell Shares":
        success = account.sell_shares(symbol, quantity)
        if success:
            return f"Sold {quantity} shares of {symbol}. Current balance: ${account.balance}", account.balance, account.holdings, account.transactions
        else:
            return "Sale failed. Insufficient shares or invalid transaction.", account.balance, account.holdings, account.transactions
    elif action == "Portfolio Value":
        return f"Total portfolio value: ${account.calculate_portfolio_value()}", account.balance, account.holdings, account.transactions
    elif action == "Profit/Loss":
        return f"Profit/Loss: ${account.calculate_profit_loss()}", account.balance, account.holdings, account.transactions
    elif action == "Report Holdings":
        return f"Holdings: {account.report_holdings()}", account.balance, account.holdings, account.transactions
    elif action == "Report Transactions":
        return f"Transactions: {account.report_transactions()}", account.balance, account.holdings, account.transactions
    else:
        return "Invalid action.", account.balance, account.holdings, account.transactions

app = gr.Interface(
    fn=dispatch_action,
    inputs=[
        gr.Dropdown([
            "Create Account",
            "Deposit",
            "Withdraw",
            "Buy Shares",
            "Sell Shares",
            "Portfolio Value",
            "Profit/Loss",
            "Report Holdings",
            "Report Transactions"
        ], label="Action"),
        gr.Number(value=default_initial_deposit, label="Initial Deposit"),
        gr.Number(value=100, label="Amount (Deposit/Withdraw)"),
        gr.Textbox(value="AAPL", label="Symbol (Buy/Sell)"),
        gr.Number(value=1, label="Quantity (Buy/Sell)")
    ],
    outputs=[
        gr.Textbox(label="Result"),
        gr.Number(label="Current Balance"),
        gr.JSON(label="Holdings"),
        gr.JSON(label="Transactions")
    ],
    title="Trading Account Management",
    description="A simple trading simulation platform to manage account transactions, portfolio value, and holdings. Select an action and fill in the relevant fields."
)

app.launch()