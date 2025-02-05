from django.shortcuts import render, get_object_or_404
from .models import Portfolio, PortfolioStock

def portfolio_detail(request, portfolio_id):
    portfolio = get_object_or_404(Portfolio, id=portfolio_id, user=request.user)
    stocks = PortfolioStock.objects.filter(portfolio=portfolio)

    for stock in stocks:
        stock.current_price = stock.current_price()
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
