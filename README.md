# Sovereign Investment Board 🕵️‍♂️💼

An AI-driven agentic system designed for institutional-grade financial analysis. The system operates through a multi-agent debate and consensus mechanism, mirroring a high-stakes investment committee. Different specialized agents cross-examine each other to rigorously vet investment ideas, manage portfolio risk, and produce actionable research.

## Usage: The Telegram-First Experience 📱

The **Sovereign Investment Board** is an agentic system designed to be operated entirely through **Telegram**. Once your bot is configured, you interact with the Board members (AI Agents) using specific slash commands.

### Primary Commands

1.  **/ticker <SYMBOL>**
    *   **Action:** Triggers a "Deep Dive Audit" of a specific stock.
    *   **Workflow:** The Engine pulls data, the Analyst reviews fundamentals, the Critic attacks the thesis, and the Chairman renders a final verdict.
    *   **Output:** You receive a visual dashboard and an Executive Brief PDF directly in your Telegram chat.

2.  **/portfolio**
    *   **Action:** Initiates a line-by-line review of your current holdings.
    *   **Workflow:** Risk audits, macro re-evaluations, and rebalancing recommendations.

3.  **/trendy**
    *   **Action:** Commands the Hunter to scout for new, emerging investment themes and present them to the Board for debate.

---

## How It Works: Behind the Scenes ⚙️

This repository provides the **Brains** (Agent Rules & Workflows) and the **Tools** (Python Scripts) for your AI Assistant.

-   **Agent Logic (`/_agent`):** Contains the persona rules and step-by-step instructions that the AI follows to act as the "Sovereign Boardroom."
-   **Execution Tools (`/scripts`):** These are the high-performance scripts the agents call to generate reports and send messages:
    -   `generate_report.py`: Creates the professional Executive Brief PDF.
    -   `visual_brief.py`: Generates the visual RSI/Valuation snapshot image.
    -   `telegram_ping.py`: The secure bridge that pushes reports to your Telegram.

## Setup & Configuration

1.  **Clone & Install**
    ```bash
    git clone https://github.com/pulkit4501/sovereign-investment-board.git
    cd sovereign-investment-board
    pip install fpdf matplotlib requests
    ```

2.  **Configure Telegram**
    Create a `.env` file or export these variables:
    ```bash
    export TELEGRAM_BOT_TOKEN="your_bot_token"
    export TELEGRAM_CHAT_ID="your_chat_id"
    ```

3.  **Connect Your Agent**
    Point your Agentic AI (e.g., GPT-4, Claude) to the rules in `/_agent/rules` and the workflows in `/_agent/workflows`. The agent will then recognize your Telegram commands and use the scripts in `/scripts` to respond.

---

## License
[MIT License](LICENSE)
