# Project Requirements

## Functional Requirements

- **Securities Management:**
  - The system manages a portfolio containing securities.
  - The portfolio supports only one type of security at a time: either stocks or bonds.

- **Transactions:**
  - **Buying:** The user can buy a stock or a bond.
  - **Selling:** The user can sell a stock or a bond.
  - Every transaction is validated against the user's defined risk tolerance.

- **Risk Management:**
  - The user sets a desired risk level for their portfolio (Low, Medium, or High).
  - A weighted risk score is calculated for the portfolio based on:
    - **Sector/Industry:**
      - Technology: 6
      - Transportation & Aviation: 5
      - Energy & Healthcare: 4
      - Industry & Finance: 3
      - Real Estate: 2
      - Consumer Goods: 1
    - **Price Volatility:**
      - Low: 1 (No major price fluctuations in the past year)
      - High: 2 (Significant price fluctuations in the past year)
    - **Bond-Specific Adjustments:**
      - Government Bonds: 50% of the default bond risk (reduced risk)
      - Corporate Bonds: Full risk factor
      - Real Estate Bonds: Minimal impact (multiplier of 0.2)
  - The final weighted risk score is classified as:
    - Low Risk: 0.1 – 2.5
    - Medium Risk: 2.51 – 4.5
    - High Risk: 4.51+

- **AI Consultation:**
  - The system integrates with a local AI agent (using an Ollama server) to answer investment-related queries.
  - The AI model is trained using relevant data (e.g., "Module 1: Introduction to Stock Markets.pdf").

- **Portfolio Visualization:**
  - The portfolio composition is displayed via a table or graph.

## Non-Functional Requirements

- **Object-Oriented Programming & Modular Design:**
  - Code is organized using OOP principles.
  - Implements a base class `Security` with derived classes:
    - **Stock:** With subtypes such as `CommonStock` and `PreferredStock`.
    - **Bond:** With subtypes such as `GovernmentBond` and `CorporateBond`.

- **MVC (Model-View-Controller) Pattern:**
  - **Model:** Classes representing securities and portfolio data.
  - **View:** A console-based REPL interface for user interaction.
  - **Controller:** Business logic for transaction processing, risk validation, and AI integration.

- **Database Integration:**
  - Use SQLite to store and retrieve transaction and portfolio data.

- **Risk Calculation Framework:**
  - Risk is computed based on sector, volatility, and security type.
  - The system ensures portfolio risk aligns with the user-defined risk level.

- **AI Integration:**
  - A local AI server (Ollama) is used to provide investment insights.
  - The AI module processes natural language queries using its trained data.

## Additional Conceptual Considerations

- Separation of Concerns (SoC)
- Abstraction, Encapsulation, and Inheritance
- Modularity (Logical & Physical)
- Use of Design Patterns (MVC, Factory, Observer)
- SOLID Principles
- Key OOP Concepts (Polymorphism, Aggregation, Dunder methods, etc.)
