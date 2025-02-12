from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Portfolio, Stock, PortfolioStock

User = get_user_model()

class PortfolioTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.portfolio = Portfolio.objects.create(name="Mon Portefeuille", user=self.user)
        self.stock = Stock.objects.create(symbol="AAPL", current_price=0.00)
        self.portfolio_stock = PortfolioStock.objects.create(
            portfolio=self.portfolio,
            stock=self.stock,
            quantity=10,
            purchase_price=150.00
        )

    def test_portfolio_creation(self):
        self.assertEqual(self.portfolio.name, "Mon Portefeuille")

    def test_stock_creation(self):
        self.assertEqual(self.stock.symbol, "AAPL")

    def test_portfolio_stock_creation(self):
        self.assertEqual(self.portfolio_stock.quantity, 10)
        self.assertEqual(self.portfolio_stock.purchase_price, 150.00)