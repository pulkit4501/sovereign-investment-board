# Sovereign Investment Board 🕵️‍♂️💼

An AI-driven agentic system designed for institutional-grade financial analysis. The system operates through a multi-agent debate and consensus mechanism, mirroring a high-stakes investment committee. Different specialized agents cross-examine each other to rigorously vet investment ideas, manage portfolio risk, and produce actionable research.

## Features

- **Multi-Agent Debate:** Eight specialized agents act as an investment committee to vet ideas.
- **Data-Driven Workflows:** Pulls financial, technical, and macro indicators to back up the narrative.
- **Executive Summaries:** Generates concise PDF and JSON Research Packs.
- **Telegram Integration:** Sends beautiful dashboards and alerts straight to your smartphone.

## Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/sovereign-investment-board.git
   cd sovereign-investment-board
   ```

2. **Install requirements**
   Ensure you have Python 3.9+ installed and required dependencies.
   ```bash
   pip install fpdf matplotlib requests
   ```

3. **Configure Environment Variables**
   For the Telegram integration to work, create a `.env` file in the root folder or export the following variables in your terminal:
   ```bash
   export TELEGRAM_BOT_TOKEN="your_telegram_bot_token"
   export TELEGRAM_CHAT_ID="your_telegram_chat_id"
   ```

## Usage

The **Sovereign Investment Board** agents handle the complex data gathering, debating, and JSON payload generation automatically under the hood. 

Once the agents produce a final research JSON, they automatically trigger these helper scripts to generate output:

**1. Generate an Executive Brief PDF:**
```bash
# The agents pass their formatted JSON string to generate a PDF.
python scripts/generate_report.py '<agent_generated_json_data>' output.pdf
```

**2. Send Alert to the Chairman:**
```bash
# Pushes the final PDF document securely to your Telegram.
python scripts/telegram_ping.py output.pdf
```

**3. Generate and Send a Visual Dashboard:**
```bash
# Creates a snapshot graphic of the stock and pushes it directly to Telegram.
python scripts/visual_brief.py '<agent_generated_json_data>'
```
