# Trading Simulation App

This directory contains a simple trading simulation platform built with Python and Gradio. The app allows you to manage a virtual trading account, perform deposits and withdrawals, buy and sell shares, and analyze your portfolio—all through an interactive web interface.

## Features

- **Account Management**: Create an account, deposit, and withdraw funds.
- **Stock Trading**: Buy and sell shares of AAPL, TSLA, and GOOGL.
- **Portfolio Analysis**: View your current holdings, transaction history, portfolio value, and profit/loss.
- **User-Friendly Interface**: Powered by Gradio for easy interaction.
- **Well-Tested**: Includes comprehensive unit tests for the core `Account` logic.

---

## File Overview

- `app.py` — Gradio web app for trading simulation
- `accounts.py` — Core `Account` class with trading logic
- `test_accounts.py` — Unit tests for the `Account` class
- `accounts.py_design.md` — Design documentation for the `Account` class

---

## Getting Started

### Prerequisites
- Python >=3.10, <3.13
- Install dependencies (from the parent directory):

```bash
uv pip install gradio
```

---

## Running the App

From this directory, launch the Gradio app:

```bash
python app.py
```

- Open your browser to the local Gradio URL (usually http://127.0.0.1:7860).
- Select an action (Create Account, Deposit, Withdraw, Buy/Sell Shares, etc.).
- Fill in the relevant fields and view results, holdings, and transaction history.

---

## Account Class Overview

The `Account` class provides methods to:
- Deposit and withdraw funds
- Buy and sell shares (with balance and holding checks)
- Calculate portfolio value and profit/loss
- Report current holdings and transaction history

See `accounts.py_design.md` for full design details.

---

## Testing

Run the unit tests to verify the core logic:

```bash
python -m unittest test_accounts.py
```

---

## License

MIT License 