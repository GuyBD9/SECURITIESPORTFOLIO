# models/bonds/bond.py
from models.security import Security

class Bond(Security):
    def __init__(self, symbol: str, name: str, price: float, industry: str = "", volatility: str = "low", bond_type: str = "corporate"):
        super().__init__(symbol, name, price)
        self.industry = industry
        self.volatility = volatility
        self.type = "bond"
        self.bond_type = bond_type  # Options: "government", "corporate", "real_estate"


