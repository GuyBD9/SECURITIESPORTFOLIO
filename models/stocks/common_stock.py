from models.stocks.stock import Stock

class CommonStock(Stock):
    def __init__(self, symbol: str, name: str, price: float, dividend_yield: float = 0.0, industry: str = "", volatility: str = "low"):
        super().__init__(symbol, name, price, dividend_yield, industry, volatility)
