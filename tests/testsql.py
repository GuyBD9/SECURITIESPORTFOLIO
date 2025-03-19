import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database.db_manager import DatabaseManager

db = DatabaseManager()
securities = db.get_all_securities()

if securities:
    print(f" Found {len(securities)} securities in the database.")
else:
    print(" No securities found. Try populating the database first.")
