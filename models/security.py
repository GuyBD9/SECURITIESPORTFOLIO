# models/security.py

class Security:
    def __init__(self, symbol: str, name: str, price: float):
        self.symbol = symbol
        self.name = name
        self.price = price

    def update_price(self, new_price: float):
        self.price = new_price

    def __str__(self):
        return f"{self.name} ({self.symbol}) - Price: {self.price}"
