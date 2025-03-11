# risk/consts.py

# Define industry risk mapping
INDUSTRY_RISK = {
    "technology": 6,
    "transportation": 5,
    "energy and health care": 4,
    "industry and finance": 3,
    "real estate": 2,
    "consumer goods": 1,
}

# Volatility factors
VOLATILITY_RISK = {
    "low": 1,
    "high": 2,
}

# Bond-specific adjustments
BOND_TYPE_ADJUSTMENT = {
    "government": 0.5,    # 50% risk factor for government bonds
    "corporate": 1.0,     # Full risk factor for corporate bonds
    "real_estate": 0.2,   # Minimal impact for real estate bonds
}
