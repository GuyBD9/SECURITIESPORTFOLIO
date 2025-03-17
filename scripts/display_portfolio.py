import matplotlib.pyplot as plt
import pandas as pd
from tabulate import tabulate
from database.db_manager import DatabaseManager

def get_portfolio_data():
    db = DatabaseManager()
    # Our securities table now has 8 columns: Symbol, Name, Price, Sector, Volatility, Type, Stock Type, Bond Type
    columns = ["Symbol", "Name", "Price", "Sector", "Volatility", "Type", "Stock Type", "Bond Type"]
    securities = db.get_all_securities()  # This returns a list of tuples
    df = pd.DataFrame(securities, columns=columns)
    
    # For demonstration, allocate an equal share percentage to each security
    if len(df) > 0:
        share_allocation = round(100.0 / len(df), 2)
        df["Share (%)"] = [share_allocation] * len(df)
    else:
        df["Share (%)"] = []
    return df

def plot_portfolio(df):
    plt.figure(figsize=(10, 6))
    # Create a bar chart using the security names and their allocated share percentage
    plt.bar(df["Name"], df["Share (%)"], color=plt.cm.Paired.colors)
    plt.xlabel("Security Name")
    plt.ylabel("Portfolio Share (%)")
    plt.title("Portfolio Composition")
    plt.xticks(rotation=45, ha="right")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.show()

def display_table(df):
    print("\nPortfolio Table:\n")
    # Display a simplified table with selected columns
    table_data = df[["Name", "Symbol", "Price", "Share (%)"]]
    print(tabulate(table_data, headers="keys", tablefmt="grid"))

def main():
    df = get_portfolio_data()
    display_table(df)
    plot_portfolio(df)

if __name__ == '__main__':
    main()
