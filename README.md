# Engineering Team Crew

Welcome to the **Engineering Team Crew** project! This repository demonstrates a multi-agent AI system using [crewAI](https://crewai.com), and includes a sample trading simulation app built with Gradio.

## Features

- **Multi-agent orchestration**: Define, configure, and run a team of AI agents to solve complex tasks collaboratively.
- **Trading Simulation App**: Simulate account management, deposits, withdrawals, stock trading, and portfolio analysis via a user-friendly Gradio web interface.
- **Well-tested Core**: The `Account` class is fully covered by unit tests.
- **Easy Customization**: Configure agents and tasks with YAML files.

---

## Directory Structure

```
engineering_team/
│
├── output/
│   ├── app.py                # Gradio trading simulation app
│   ├── accounts.py           # Account class for trading logic
│   ├── test_accounts.py      # Unit tests for Account
│   └── accounts.py_design.md # Design documentation for Account
│
├── src/engineering_team/
│   ├── main.py               # Main entry point for crewAI
│   ├── crew.py               # Crew and agent/task logic
│   └── config/
│       ├── agents.yaml       # Agent definitions
│       └── tasks.yaml        # Task definitions
│
├── pyproject.toml            # Project dependencies and metadata
└── README.md                 # This file
```

---

## Getting Started

### Prerequisites

- Python >=3.10, <3.13
- [UV](https://docs.astral.sh/uv/) for dependency management

### Installation

```bash
pip install uv
cd 3_crew/engineering_team
uv pip install -r requirements.txt
```

Or, if using `pyproject.toml`:

```bash
uv pip install .
```

### Environment Variables

If using OpenAI or other APIs, add your keys to a `.env` file as needed.

---

## Running the Trading Simulation App

The trading simulation app is in `output/app.py` and provides a web interface for account operations.

```bash
cd output
python app.py
```

- Open your browser to the local Gradio URL (usually http://127.0.0.1:7860).
- Select an action (Create Account, Deposit, Withdraw, Buy/Sell Shares, etc.).
- Fill in the relevant fields and view results, holdings, and transaction history.

### App Features

- **Create Account**: Start a new account with an initial deposit.
- **Deposit/Withdraw**: Manage your account balance.
- **Buy/Sell Shares**: Trade stocks (AAPL, TSLA, GOOGL).
- **Portfolio Value & Profit/Loss**: Analyze your investments.
- **Holdings & Transactions**: View your current stocks and trade history.

---

## Account Class

The `Account` class (see `output/accounts.py`) provides:

- Deposit and withdraw methods
- Buy and sell shares with balance and holding checks
- Portfolio value and profit/loss calculation
- Holdings and transaction reporting

See `accounts.py_design.md` for full design details.

---

## Testing

Unit tests for the `Account` class are in `output/test_accounts.py`:

```bash
cd output
python -m unittest test_accounts.py
```

---

## Customizing Agents and Tasks

- Edit `src/engineering_team/config/agents.yaml` to define your agents.
- Edit `src/engineering_team/config/tasks.yaml` to define your tasks.
- Modify `src/engineering_team/crew.py` and `main.py` for advanced logic.

To run the crewAI system:

```bash
cd ..
crewai run
```

---

## Contributing

Pull requests and issues are welcome! Please open an issue to discuss your ideas or report bugs.

---

## License

MIT License

---

## Support

- [crewAI Documentation](https://docs.crewai.com)
- [crewAI GitHub](https://github.com/joaomdmoura/crewai)
- [Discord Community](https://discord.com/invite/X4JWnZnxPb)
