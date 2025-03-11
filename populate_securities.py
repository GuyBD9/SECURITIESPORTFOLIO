# populate_securities.py
from database.db_manager import DatabaseManager

def populate_securities():
    db = DatabaseManager()
    
    # Insert sample common stocks
    db.insert_security("AAPL", "Apple Inc.", 150.0, "technology", "high", "stock")
    db.insert_security("MSFT", "Microsoft Corporation", 300.0, "technology", "high", "stock")
    db.insert_security("GOOG", "Alphabet Inc.", 2800.0, "technology", "high", "stock")
    db.insert_security("TSLA", "Tesla Inc.", 700.0, "transportation", "high", "stock")
    db.insert_security("AMZN", "Amazon.com Inc.", 3400.0, "industry and finance", "high", "stock")
    db.insert_security("NFLX", "Netflix Inc.", 500.0, "technology", "high", "stock")
    db.insert_security("DIS", "Disney", 90.0, "consumer goods", "low", "stock")
    db.insert_security("FB", "Meta Platforms", 200.0, "technology", "high", "stock")
    
    # Insert a sample preferred stock (treated as a stock)
    db.insert_security("PGP", "Procter & Gamble Preferred", 140.0, "consumer goods", "low", "stock")
    
    # Insert bonds
    db.insert_security("USGOV", "US Government Bond", 100.0, "industry and finance", "low", "bond", "government")
    db.insert_security("UKGOV", "UK Government Bond", 100.0, "industry and finance", "low", "bond", "government")
    db.insert_security("CORP1", "Corporate Bond 1", 100.0, "industry and finance", "high", "bond", "corporate")
    db.insert_security("CORP2", "Corporate Bond 2", 95.0, "industry and finance", "high", "bond", "corporate")
    db.insert_security("REBD", "Real Estate Bond", 102.0, "real estate", "low", "bond", "real_estate")
    db.insert_security("CORP3", "Corporate Bond 3", 105.0, "industry and finance", "high", "bond", "corporate")
    
    print("Database has been populated with sample securities.")

if __name__ == "__main__":
    populate_securities()
