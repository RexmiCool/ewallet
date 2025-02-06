from django.shortcuts import render, get_object_or_404
from .models import Portfolio, PortfolioStock

def portfolio_detail(request, portfolio_id):
    portfolio = get_object_or_404(Portfolio, id=portfolio_id, user=request.user)
    stocks = PortfolioStock.objects.filter(portfolio=portfolio)

    for stock in stocks:
        stock.current_price = stock.current_price()  # Appel de la méthode pour obtenir le prix actuel
        stock.profit_data = stock.profit_loss()

    return render(request, "finance/portfolio_detail.html", {"portfolio": portfolio, "stocks": stocks})

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Portfolio

class PortfolioListView(LoginRequiredMixin, ListView):
    model = Portfolio
    template_name = "finance/portfolio_list.html"
    context_object_name = "portfolios"

    def get_queryset(self):
        return Portfolio.objects.filter(user=self.request.user)

class PortfolioCreateView(LoginRequiredMixin, CreateView):
    model = Portfolio
    fields = ["name"]
    template_name = "finance/portfolio_form.html"
    success_url = reverse_lazy("portfolio_list")

    def form_valid(self, form):
        form.instance.user = self.request.user  # Associer l'utilisateur connecté
        return super().form_valid(form)


from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Stock, PortfolioStock
from .services.stock_api import get_stock_price

def add_stock(request, portfolio_id):
    if request.method == 'POST':
        symbol = request.POST['symbol']
        quantity = request.POST['quantity']
        purchase_price = request.POST['purchase_price']
        
        # Appel à l'API pour obtenir le prix actuel de l'action
        current_price = get_stock_price(symbol)
        
        if current_price is None:
            # Gérer le cas où le prix actuel n'est pas disponible
            #return render(request, 'finance/portfolio_detail.html', {'error': 'Prix actuel non disponible pour cette action.'})
            portfolio = get_object_or_404(Portfolio, id=portfolio_id, user=request.user)
            stocks = PortfolioStock.objects.filter(portfolio=portfolio)

            for stock in stocks:
                stock.current_price = stock.current_price()  # Appel de la méthode pour obtenir le prix actuel
                stock.profit_data = stock.profit_loss()

            return render(request, "finance/portfolio_detail.html", {"portfolio": portfolio, "stocks": stocks})
        # Enregistrer l'action dans la base de données
        stock = Stock(symbol=symbol, current_price=current_price)
        stock.save()

        portfolio_stock = PortfolioStock(portfolio_id=portfolio_id, stock=stock, quantity=quantity, purchase_price=purchase_price)
        portfolio_stock.save()
        
        return redirect(reverse('portfolio_detail', args=[portfolio_id]))
    portfolio = get_object_or_404(Portfolio, id=portfolio_id, user=request.user)
    stocks = PortfolioStock.objects.filter(portfolio=portfolio)

    for stock in stocks:
        stock.current_price = stock.current_price()  # Appel de la méthode pour obtenir le prix actuel
        stock.profit_data = stock.profit_loss()

    return render(request, "finance/portfolio_detail.html", {"portfolio": portfolio, "stocks": stocks})
    #return render(request, 'finance/add_stock.html')