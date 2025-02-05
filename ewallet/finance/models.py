from django.db import models
from django.conf import settings
from .services.stock_api import get_stock_price


class Portfolio(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Stock(models.Model):
    symbol = models.CharField(max_length=10, unique=True)  # Ex: AAPL, MSFT
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} ({self.symbol})"

class PortfolioStock(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)  # Prix d'achat par action
    purchase_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} x {self.stock.symbol} dans {self.portfolio.name}"

    def current_price(self):
        """ Récupère le prix actuel de l'action """
        return get_stock_price(self.stock.symbol)

    def profit_loss(self):
        """ Calcule la plus-value en valeur et en pourcentage """
        current_price = self.current_price()
        if current_price:
            total_purchase = self.quantity * self.purchase_price
            total_current = self.quantity * current_price
            return {
                "profit": total_current - total_purchase,
                "profit_percent": ((total_current - total_purchase) / total_purchase) * 100
            }
        return None  # Si l'API ne renvoie pas de prix
