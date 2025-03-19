def start_repl(portfolio_controller, ai_controller):
    print("Welcome to the Securities Investment Manager!")
    print("Commands: setrisk <level>, buy <type> <symbol> <quantity>, sell <symbol> <quantity>, ai <question>, show portfolio, show securities, exit")
    
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

            result = portfolio_controller.buy_security(sec_type, symbol, qty)
            print(result)
        elif command.startswith("sell"):
            parts = command.split()
            if len(parts) != 3:
                print("Invalid command. Usage: sell <symbol> <quantity>")
                continue
            _, symbol, qty = parts
            try:
                qty = int(qty)
            except ValueError:
                print("Quantity must be an integer.")
                continue

            result = portfolio_controller.sell_security(symbol, qty)
            print(result)
        elif command.startswith("ai"):
            question = command[3:].strip()
            answer = ai_controller.consult_ai(question)
            print("AI Response:", answer)
        elif command.startswith("show portfolio"):
            portfolio_summary = portfolio_controller.get_portfolio_summary()
            print(portfolio_summary)
        elif command.startswith("show securities"):
            from concurrent.futures import ThreadPoolExecutor
            from database.db_manager import DatabaseManager
            from tabulate import tabulate

            executor = ThreadPoolExecutor(max_workers=5)
            db = DatabaseManager()

            future = executor.submit(db.get_all_securities)
            securities = future.result()

            if securities:
                headers = ["Symbol", "Name", "Price", "Sector", "Volatility", "Type", "Bond Type"]
                print(tabulate(securities, headers=headers, tablefmt="grid"))
            else:
                print("No securities found in the database.")
        else:
            print("Unknown command. Please try again.")
