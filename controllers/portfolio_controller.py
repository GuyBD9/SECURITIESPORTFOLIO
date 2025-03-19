from database.db_manager import DatabaseManager
from models.stocks.common_stock import CommonStock
from models.bonds.corporate_bond import CorporateBond
from risk.risk_calculator import calculate_portfolio_risk, classify_risk

class PortfolioController:
    def __init__(self, risk_level: str):
        self.db_manager = DatabaseManager()  # Manages database operations
        self.risk_level = risk_level  # "Low Risk", "Medium Risk", "High Risk"
        self.portfolio = {}  # Dictionary mapping security objects to quantities

    def set_risk_level(self, level: str):
        """Sets the risk level for the portfolio."""
        self.risk_level = level

    def buy_security(self, sec_type: str, symbol: str, quantity: int):
        """
        Purchases a security based on data from the database instead of using hardcoded values.
        """
        # Fetch security data from the database
        security_data = self.db_manager.get_security(symbol)

        if not security_data:
            return f"⚠️ Error: Security '{symbol}' not found in database."

        # Extract data from query result
        symbol, name, price, sector, volatility, sec_type, stock_type, bond_type = security_data

        # Create the appropriate object based on security type
        if sec_type == "stock":
            security = CommonStock(symbol, name, price, industry=sector, volatility=volatility)
        elif sec_type == "bond":
            security = CorporateBond(symbol, name, price, industry=sector, volatility=volatility)
        else:
            return "⚠️ Error: Unknown security type."

        # Update the portfolio
        self.portfolio[security] = self.portfolio.get(security, 0) + quantity
        self.db_manager.save_transaction('buy', security, quantity)
        
        # Calculate portfolio risk
        current_risk = calculate_portfolio_risk(self.portfolio)
        risk_category = classify_risk(current_risk)
        
        if risk_category != self.risk_level:
            return (f"✅ Bought {quantity} of {security.name}. "
                    f"Portfolio risk: {risk_category} (score: {current_risk:.2f}). "
                    f"Mismatch with selected risk: {self.risk_level}.")
        else:
            return (f"✅ Bought {quantity} of {security.name}. "
                    f"Portfolio risk is aligned: {risk_category} (score: {current_risk:.2f}).")
    
    def sell_security(self, symbol: str, quantity: int):
        """Sells a security from the portfolio."""
        for security in self.portfolio.keys():
            if security.symbol == symbol:
                if self.portfolio[security] < quantity:
                    return f"⚠️ Error: Not enough {symbol} to sell."
                
                self.portfolio[security] -= quantity
                self.db_manager.save_transaction('sell', security, quantity)
                
                if self.portfolio[security] == 0:
                    del self.portfolio[security]
                
                return f"✅ Sold {quantity} of {symbol}. Portfolio updated."
        
        return f"⚠️ Error: Security '{symbol}' not found in portfolio."
    
    def get_portfolio_summary(self):
        """Returns a summary of the portfolio."""
        if not self.portfolio:
            return "Portfolio is empty."
        
        summary = "\nPortfolio Summary:\n"
        for security, quantity in self.portfolio.items():
            summary += f"{security.name} ({security.symbol}): {quantity} shares\n"
        
        return summary
