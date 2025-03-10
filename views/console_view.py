# views/console_view.py
from controllers.portfolio_controller import PortfolioController
from controllers.ai_controller import AIController
from models.stock import CommonStock
from models.bond import CorporateBond

def start_repl():
    # Default risk level can be set to "Low Risk", "Medium Risk", or "High Risk"
    portfolio_controller = PortfolioController(risk_level="Low Risk")
    ai_controller = AIController()

    print("Welcome to the Securities Investment Manager!")
    print("Commands: setrisk <level>, buy <type> <symbol> <quantity>, sell <type> <symbol> <quantity>, ai <question>, show portfolio, exit")
    
    while True:
        command = input(">> ").strip().lower()
        if command in ['exit', 'quit']:
            print("Exiting... Goodbye!")
            break
        elif command.startswith("setrisk"):
            try:
                _, level = command.split()
                portfolio_controller.set_risk_level(level.capitalize() + " Risk")
                print(f"Risk level set to: {portfolio_controller.risk_level}")
            except ValueError:
                print("Usage: setrisk <low|medium|high>")
        elif command.startswith("buy"):
            parts = command.split()
            if len(parts) != 4:
                print("Invalid command. Usage: buy <stock|bond> <symbol> <quantity>")
                continue
            _, sec_type, symbol, qty = parts
            try:
                qty = int(qty)
            except ValueError:
                print("Quantity must be an integer.")
                continue

            if sec_type == "stock":
                # For demonstration, create a CommonStock with sample data.
                security = CommonStock(symbol, "Example Stock", price=100, industry="real estate", volatility="low")
            elif sec_type == "bond":
                security = CorporateBond(symbol, "Example Bond", price=1000, industry="industry and finance", volatility="high")
            else:
                print("Unknown security type. Use 'stock' or 'bond'.")
                continue
            result = portfolio_controller.buy_security(security, qty)
            print(result)
        elif command.startswith("ai"):
            question = command[3:].strip()
            answer = ai_controller.consult_ai(question)
            print("AI Response:", answer)
        elif command.startswith("show portfolio"):
            if portfolio_controller.portfolio:
                print("Current Portfolio:")
                for sec, qty in portfolio_controller.portfolio.items():
                    print(f"  {sec} : {qty}")
            else:
                print("Portfolio is empty.")
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    start_repl()
