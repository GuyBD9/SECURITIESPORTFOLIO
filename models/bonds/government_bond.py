from bond import Bond

class GovernmentBond(Bond):
    def __init__(self, symbol: str, name: str, price: float, industry: str = "", volatility: str = "low"):
        super().__init__(symbol, name, price, industry, volatility, bond_type="government")
