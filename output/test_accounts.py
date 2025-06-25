import unittest
from accounts import Account

class TestAccount(unittest.TestCase):

    def setUp(self):
        self.account = Account(user_id="user123", initial_deposit=1000.0)

    def test_deposit(self):
        self.account.deposit(500.0)
        self.assertEqual(self.account.balance, 1500.0)

    def test_deposit_negative_amount(self):
        self.account.deposit(-100.0)
        self.assertEqual(self.account.balance, 1000.0)

    def test_withdraw(self):
        result = self.account.withdraw(200.0)
        self.assertTrue(result)
        self.assertEqual(self.account.balance, 800.0)

    def test_withdraw_insufficient_balance(self):
        result = self.account.withdraw(1200.0)
        self.assertFalse(result)
        self.assertEqual(self.account.balance, 1000.0)

    def test_withdraw_negative_amount(self):
        result = self.account.withdraw(-50.0)
        self.assertFalse(result)
        self.assertEqual(self.account.balance, 1000.0)

    def test_buy_shares(self):
        result = self.account.buy_shares('AAPL', 5)
        self.assertTrue(result)
        self.assertEqual(self.account.balance, 250.0)
        self.assertEqual(self.account.holdings, {'AAPL': 5})

    def test_buy_shares_insufficient_funds(self):
        result = self.account.buy_shares('GOOGL', 1)
        self.assertFalse(result)
        self.assertEqual(self.account.holdings, {})

    def test_buy_shares_negative_quantity(self):
        result = self.account.buy_shares('TSLA', -3)
        self.assertFalse(result)
        self.assertEqual(self.account.holdings, {})

    def test_sell_shares(self):
        self.account.buy_shares('AAPL', 5)
        result = self.account.sell_shares('AAPL', 3)
        self.assertTrue(result)
        self.assertEqual(self.account.holdings, {'AAPL': 2})
        self.assertEqual(self.account.balance, 700.0)

    def test_sell_shares_not_owned(self):
        result = self.account.sell_shares('AAPL', 1)
        self.assertFalse(result)
        self.assertEqual(self.account.holdings, {})

    def test_sell_shares_negative_quantity(self):
        self.account.buy_shares('AAPL', 5)
        result = self.account.sell_shares('AAPL', -2)
        self.assertFalse(result)
        self.assertEqual(self.account.holdings, {'AAPL': 5})

    def test_calculate_portfolio_value(self):
        self.account.buy_shares('TSLA', 2)
        portfolio_value = self.account.calculate_portfolio_value()
        expected_value = self.account.balance + 2 * 700.0
        self.assertEqual(portfolio_value, expected_value)

    def test_calculate_profit_loss(self):
        self.account.buy_shares('AAPL', 4)
        profit_loss = self.account.calculate_profit_loss()
        expected_profit_loss = self.account.calculate_portfolio_value() - 1000.0
        self.assertEqual(profit_loss, expected_profit_loss)

    def test_report_holdings(self):
        self.account.buy_shares('TSLA', 2)
        holdings = self.account.report_holdings()
        self.assertEqual(holdings, {'TSLA': 2})

    def test_report_transactions(self):
        self.account.buy_shares('AAPL', 2)
        self.account.sell_shares('AAPL', 1)
        transactions = self.account.report_transactions()
        expected_transactions = [
            {'action': 'buy', 'symbol': 'AAPL', 'quantity': 2, 'price': 150.0},
            {'action': 'sell', 'symbol': 'AAPL', 'quantity': 1, 'price': 150.0}
        ]
        self.assertEqual(transactions, expected_transactions)

if __name__ == '__main__':
    unittest.main()