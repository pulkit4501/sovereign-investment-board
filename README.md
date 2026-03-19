# Sovereign Investment Board 🕵️‍♂️💼

An AI-driven agentic system designed for institutional-grade financial analysis. The system operates through a multi-agent debate and consensus mechanism, mirroring a high-stakes investment committee. Different specialized agents cross-examine each other to rigorously vet investment ideas, manage portfolio risk, and produce actionable research.

// Kindly note that the solution PDF is being refined and the updates should be out soon

## Usage: The Sovereign Investment Board 📱🕵️‍♂️

This repository is designed to be used in **AI-powered environments** (like Cursor, VS Code with Copilot, or specialized Agentic IDEs). 

### 1. How to Interact with the Board
Simply open this repository in your AI-powered IDE. The AI will automatically leverage the **Rules** and **Workflows** in the `/_agent/` directory to act as your Investment Board. 

You can then type commands directly into your AI chat:
-   **/ticker <SYMBOL>**: Triggers a Deep Dive Audit (e.g., `/ticker AAPL`).
-   **/portfolio**: Initiates a full performance and risk review of your holdings.
-   **/trendy**: Commands the Board to scout for new emerging market themes.

### 2. Portfolio Management (CSV)
For the `/portfolio` command to work, the Board needs to know what you own.
1.  **Create/Update:** Ensure there is a file named `current_portfolio.csv` in the root directory.
2.  **Format:** Use the following headers: `Ticker, Quantity, Average Price, Sector`.
3.  **Sync:** Whenever you buy or sell, update this CSV and the Board will reflect the changes in the next `/portfolio` audit.

---

## How It Works: Behind the Scenes ⚙️

-   **Agent Logic (`/_agent`):** The "Brains" of the system. Contains the persona rules and persona-driven workflows.
-   **Execution Tools (`/scripts`):** The "Muscle" of the system. High-performance Python scripts that the agents call to:
    -   `generate_report.py`: Create professional Executive Brief PDFs.
    -   `visual_brief.py`: Generate visual RSI/Valuation snapshot images.
    -   `telegram_ping.py`: Securely push all reports and alerts to your Telegram.

## Setup & Configuration

1.  **Clone & Install**
    ```bash
    git clone https://github.com/pulkit4501/sovereign-investment-board.git
    cd sovereign-investment-board
    pip install fpdf matplotlib requests
    ```

2.  **Configure Telegram**
    To receive alerts on your phone, create a `.env` file or export these variables:
    ```bash
    export TELEGRAM_BOT_TOKEN="your_bot_token"
    export TELEGRAM_CHAT_ID="your_chat_id"
    ```

---


