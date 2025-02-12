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
    symbol = models.CharField(max_length=10)
    current_price = models.FloatField()
    def __str__(self):
        return f"({self.symbol})"

from .services.stock_api import get_stock_price

class PortfolioStock(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    purchase_price = models.FloatField()

    def current_price(self):
        """ Récupère le prix actuel de l'action """
        return get_stock_price(self.stock.symbol)

    def profit_loss(self):
        """ Calcule la plus-value en valeur et en pourcentage """
        current_price = get_stock_price(self.stock.symbol)
        if current_price:
            total_purchase = float(self.quantity * self.purchase_price)
            total_current = float(self.quantity * current_price)
            return {
                "profit": total_current - total_purchase,
                "profit_percent": ((total_current - total_purchase) / total_purchase) * 100
            }
        return None  # Si l'API ne renvoie pas de prix
