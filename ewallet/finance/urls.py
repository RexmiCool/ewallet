from django.urls import path
from .views import portfolio_detail, PortfolioListView, PortfolioCreateView

urlpatterns = [
    path('portfolio/<int:portfolio_id>/', portfolio_detail, name='portfolio_detail'),
    path("portfolios/", PortfolioListView.as_view(), name="portfolio_list"),
    path("portfolios/new/", PortfolioCreateView.as_view(), name="portfolio_create"),
]

