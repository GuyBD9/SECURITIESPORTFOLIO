# High-Level Architecture Design

## System Architecture Overview

The system is built using the MVC (Model-View-Controller) pattern, with the following layers:

- **Model Layer:**
  - **Security (Base Class):**
    - Attributes: `symbol`, `name`, `price`
    - Methods: `update_price()`, `__str__()`
  - **Stock:**
    - Inherits from `Security` and includes additional attributes (e.g., `dividend_yield`, `industry`, `volatility`).
    - Subtypes:
      - `CommonStock`
      - `PreferredStock`
  - **Bond:**
    - Inherits from `Security` and includes attributes such as `coupon_rate`, `maturity`, `industry`, `volatility`, and `bond_type`.
    - Subtypes:
      - `GovernmentBond`
      - `CorporateBond`

- **Controller Layer:**
  - **Portfolio Controller:**
    - Manages buying and selling of securities.
    - Updates portfolio composition.
    - Validates portfolio risk against the user-defined risk level using the risk module.
  - **AI Controller:**
    - Interacts with the AI module to process natural language queries.
    - Retrieves investment advice from the local Ollama server.

- **View Layer:**
  - Provides a console-based REPL interface.
  - Processes commands such as `setrisk`, `buy`, `sell`, `ai`, and `show portfolio`.

- **Risk Module:**
  - Contains functions to calculate risk for individual securities and the entire portfolio.
  - Uses predefined mappings for industry risk, volatility factors, and bond-specific adjustments.
  - Classifies the portfolio risk into Low, Medium, or High categories.

- **Database Layer:**
  - Implements SQLite integration.
  - Manages transaction records and portfolio data through CRUD operations.

- **AI Module:**
  - Provides an interface to communicate with the local Ollama AI server.
  - Processes investment-related queries.

## Physical Project Structure

The project directory is organized as follows:

