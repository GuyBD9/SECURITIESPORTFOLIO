# models/stock.py
from models.security import Security

class Stock(Security):
    def __init__(self, symbol: str, name: str, price: float, dividend_yield: float = 0.0, industry: str = "", volatility: str = "low"):
        super().__init__(symbol, name, price)
        self.dividend_yield = dividend_yield
        self.industry = industry    # e.g., "technology", "real estate", etc.
        self.volatility = volatility  # "low" or "high"
        self.type = "stock"         # For risk calculations


