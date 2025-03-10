from .consts import INDUSTRY_RISK, VOLATILITY_RISK, BOND_TYPE_ADJUSTMENT


def calculate_security_risk(security):
    """
    Calculate the risk of a single security based on its industry and volatility.
    Expects the security object to have:
      - industry (string)
      - volatility (string: "low" or "high")
      - type (either "stock" or "bond")
      - For bonds, a bond_type attribute ("government", "corporate", or "real_estate")
    """
    industry = getattr(security, "industry", "").lower()
    industry_risk = INDUSTRY_RISK.get(industry, 0)
    
    volatility = getattr(security, "volatility", "low").lower()
    volatility_factor = VOLATILITY_RISK.get(volatility, 1)
    
    base_risk = industry_risk * volatility_factor
    
    if getattr(security, "type", "stock").lower() == "bond":
        bond_type = getattr(security, "bond_type", "corporate").lower()
        adjustment = BOND_TYPE_ADJUSTMENT.get(bond_type, 1.0)
        adjusted_risk = base_risk * adjustment
    else:
        adjusted_risk = base_risk

    return adjusted_risk

def calculate_portfolio_risk(portfolio):
    """
    Calculate a weighted risk score for the portfolio.
    'portfolio' is a dictionary mapping security objects to quantities.
    """
    total_risk = 0
    total_quantity = 0
    for security, quantity in portfolio.items():
        risk = calculate_security_risk(security)
        total_risk += risk * quantity
        total_quantity += quantity
    return total_risk / total_quantity if total_quantity else 0

def classify_risk(risk_score):
    """
    Classify the final risk score into user-defined levels.
    """
    if risk_score < 0.1:
        return "Undefined"
    elif 0.1 <= risk_score <= 2.5:
        return "Low Risk"
    elif 2.51 <= risk_score <= 4.5:
        return "Medium Risk"
    else:
        return "High Risk"
