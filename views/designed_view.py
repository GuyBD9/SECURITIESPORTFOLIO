# views/designed_view.py
import sys
from tabulate import tabulate
from colorama import Fore, Style, init
from controllers.portfolio_controller import PortfolioController
from controllers.ai_controller import AIController
from models.stocks.common_stock import CommonStock
from models.bonds.corporate_bond import CorporateBond

# Initialize colorama for colored terminal output
init(autoreset=True)

def print_banner():
    print(Fore.CYAN + "=" * 60)
    print(Fore.YELLOW + " Welcome to the Securities Investment Manager ".center(60, "="))
    print(Fore.CYAN + "=" * 60)
    print(Fore.GREEN + "Available Commands:")
    commands = [
        ["setrisk <low|medium|high>", "Set portfolio risk level"],
        ["buy <stock|bond> <symbol> <quantity>", "Buy securities"],
        ["sell <stock|bond> <symbol> <quantity>", "Sell securities"],
        ["ai <question>", "Consult AI for investment advice"],
        ["show portfolio", "Display current portfolio"],
        ["show securities", "List available securities"],
        ["exit", "Exit the program"]
    ]
    print(tabulate(commands, headers=["Command", "Description"], tablefmt="fancy_grid"))
    print()

def handle_setrisk(portfolio_controller, command):
    try:
        _, level = command.split()
        level = level.capitalize() + " Risk"
        portfolio_controller.set_risk_level(level)
        print(Fore.GREEN + f"Risk level set to: {portfolio_controller.risk_level}")
    except ValueError:
        print(Fore.RED + "Usage: setrisk <low|medium|high>")

def handle_buy(portfolio_controller, command):
    parts = command.split()
    if len(parts) != 4:
        print(Fore.RED + "Invalid command. Usage: buy <stock|bond> <symbol> <quantity>")
        return
    _, sec_type, symbol, qty = parts
    try:
        qty = int(qty)
    except ValueError:
        print(Fore.RED + "Quantity must be an integer.")
        return

    if sec_type == "stock":
        security = CommonStock(symbol, "Example Stock", price=100, industry="Real Estate", volatility="Low")
    elif sec_type == "bond":
        security = CorporateBond(symbol, "Example Bond", price=1000, industry="Industry and Finance", volatility="High")
    else:
        print(Fore.RED + "Unknown security type. Use 'stock' or 'bond'.")
        return
    
    result = portfolio_controller.buy_security(security, qty)
    print(Fore.GREEN + result)

def handle_ai(ai_controller, command):
    question = command[3:].strip()
    answer = ai_controller.consult_ai(question)
    print(Fore.MAGENTA + "AI Response: " + Fore.YELLOW + answer)

def handle_show_portfolio(portfolio_controller):
    if portfolio_controller.portfolio:
        print(Fore.CYAN + "\nCurrent Portfolio:")
        portfolio_data = [[str(sec), qty] for sec, qty in portfolio_controller.portfolio.items()]
        print(tabulate(portfolio_data, headers=["Security", "Quantity"], tablefmt="fancy_grid"))
    else:
        print(Fore.YELLOW + "Portfolio is empty.")

def handle_show_securities():
    from database.db_manager import DatabaseManager
    db = DatabaseManager()
    securities = db.get_all_securities()
    if securities:
        headers = ["Symbol", "Name", "Price", "Sector", "Volatility", "Type", "Stock Type", "Bond Type"]
        print(Fore.CYAN + "\nAvailable Securities:")
        print(tabulate(securities, headers=headers, tablefmt="fancy_grid"))
    else:
        print(Fore.RED + "No securities found in the database.")

def start_repl():
    portfolio_controller = PortfolioController(risk_level="Low Risk")
    ai_controller = AIController()

    print_banner()

    while True:
        command = input(Fore.BLUE + ">> " + Style.RESET_ALL).strip().lower()
        if command in ['exit', 'quit']:
            print(Fore.RED + "Exiting... Goodbye!")
            sys.exit()
        elif command.startswith("setrisk"):
            handle_setrisk(portfolio_controller, command)
        elif command.startswith("buy"):
            handle_buy(portfolio_controller, command)
        elif command.startswith("ai"):
            handle_ai(ai_controller, command)
        elif command.startswith("show portfolio"):
            handle_show_portfolio(portfolio_controller)
        elif command.startswith("show securities"):
            handle_show_securities()
        else:
            print(Fore.RED + "Unknown command. Please try again.")

if __name__ == "__main__":
    start_repl()
