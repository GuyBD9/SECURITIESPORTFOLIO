# controllers/portfolio_controller.py
from database.db_manager import DatabaseManager
from risk.risk_calculator import calculate_portfolio_risk, classify_risk

class PortfolioController:
    def __init__(self, risk_level: str):
        self.db_manager = DatabaseManager()  # Handles database operations
        self.risk_level = risk_level  # e.g., "Low Risk", "Medium Risk", "High Risk"
        self.portfolio = {}  # Dictionary: {security_object: quantity}

    def set_risk_level(self, level: str):
        self.risk_level = level

    def buy_security(self, security, quantity):
        self.portfolio[security] = self.portfolio.get(security, 0) + quantity
        self.db_manager.save_transaction('buy', security, quantity)
        current_risk = calculate_portfolio_risk(self.portfolio)
        risk_category = classify_risk(current_risk)
        if risk_category != self.risk_level:
            return (f"Bought {quantity} of {security.name}. "
                    f"Portfolio risk: {risk_category} (score: {current_risk:.2f}). "
                    f"Mismatch with selected risk: {self.risk_level}.")
        else:
            return (f"Bought {quantity} of {security.name}. "
                    f"Portfolio risk is aligned: {risk_category} (score: {current_risk:.2f}).")
