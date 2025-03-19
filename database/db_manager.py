import sqlite3
from threading import Lock

class DatabaseManager:
    _instance = None
    _lock = Lock()

    def __new__(cls, db_file='portfolio.db'):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(DatabaseManager, cls).__new__(cls)
                cls._instance.conn = sqlite3.connect(db_file, check_same_thread=False)
                cls._instance.cursor = cls._instance.conn.cursor()
                cls._instance.create_tables()
                cls._instance.create_securities_table()
        return cls._instance

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

    def execute_query(self, query, params=()):
        """ Executes a query without returning a result (INSERT, UPDATE, DELETE) """
        with self._lock:
            self.cursor.execute(query, params)
            self.conn.commit()

    def fetch_all(self, query, params=()):
        """ Executes a SELECT query and returns all results """
        with self._lock:
            self.cursor.execute(query, params)
            return self.cursor.fetchall()

    def fetch_one(self, query, params=()):
        """ Executes a SELECT query and returns a single result """
        with self._lock:
            self.cursor.execute(query, params)
            return self.cursor.fetchone()

    def insert_security(self, symbol, name, price, sector, volatility, sec_type, stock_type=None, bond_type=None):
        """
        Inserts or updates a security record in the securities table.
        """
        self.execute_query("""
            INSERT OR REPLACE INTO securities (symbol, name, price, sector, volatility, type, stock_type, bond_type)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (symbol, name, price, sector, volatility, sec_type, stock_type, bond_type))

    def get_security(self, symbol):
        symbol = symbol.upper()
        return self.fetch_one("""
            SELECT symbol, name, price, sector, volatility, type, stock_type, bond_type 
            FROM securities 
            WHERE UPPER(symbol) = ?
        """, (symbol,))

    def get_all_securities(self):
        return self.fetch_all("""
            SELECT symbol, name, price, sector, volatility, type, stock_type, bond_type 
            FROM securities
        """)

    def save_transaction(self, action, security, quantity):
        self.execute_query("""
            INSERT INTO transactions (action, symbol, quantity) VALUES (?, ?, ?)
        """, (action, security.symbol, quantity))

    def get_all_transactions(self):
        """ Retrieves all transactions from the database. """
        return self.fetch_all("""
            SELECT id, action, symbol, quantity, timestamp 
            FROM transactions
        """)

    def close_connection(self):
        with self._lock:
            self.conn.close()
