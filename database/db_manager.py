# database/db_manager.py
import sqlite3

class DatabaseManager:
    def __init__(self, db_file='portfolio.db'):
        self.conn = sqlite3.connect(db_file)
        self.create_tables()
        self.create_securities_table()  # Create the new table for securities

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

    def create_securities_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS securities (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                symbol TEXT UNIQUE,
                name TEXT,
                price REAL,
                sector TEXT,
                volatility TEXT,
                type TEXT,         -- "stock" or "bond"
                stock_type TEXT,   -- "common" or "preferred" for stocks (NULL for bonds)
                bond_type TEXT     -- "government", "corporate", etc. (NULL for stocks)
            )
        """)
        self.conn.commit()

    def insert_security(self, symbol, name, price, sector, volatility, sec_type, stock_type=None, bond_type=None):
        """
        Inserts or updates a security record in the securities table.
        """
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT OR REPLACE INTO securities (symbol, name, price, sector, volatility, type, stock_type, bond_type)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (symbol, name, price, sector, volatility, sec_type, stock_type, bond_type))
        self.conn.commit()

    def get_security(self, symbol):
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT symbol, name, price, sector, volatility, type, stock_type, bond_type 
            FROM securities 
            WHERE symbol=?
        """, (symbol,))
        return cursor.fetchone()

    def get_all_securities(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT symbol, name, price, sector, volatility, type, stock_type, bond_type 
            FROM securities
        """)
        return cursor.fetchall()

    def save_transaction(self, action, security, quantity):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO transactions (action, symbol, quantity) VALUES (?, ?, ?)",
                       (action, security.symbol, quantity))
        self.conn.commit()
