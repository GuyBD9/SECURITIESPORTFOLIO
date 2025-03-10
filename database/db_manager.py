# database/db_manager.py
import sqlite3

class DatabaseManager:
    def __init__(self, db_file='portfolio.db'):
        self.conn = sqlite3.connect(db_file)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                action TEXT,
                symbol TEXT,
                quantity INTEGER,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.conn.commit()

    def save_transaction(self, action, security, quantity):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO transactions (action, symbol, quantity) VALUES (?, ?, ?)",
                       (action, security.symbol, quantity))
        self.conn.commit()
