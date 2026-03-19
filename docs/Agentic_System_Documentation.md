# Sovereign Investment Board - Agentic System Overview

## 1. Executive Summary
This document outlines the architecture and operation of the "Sovereign Investment Board," an AI-driven agentic system designed for institutional-grade financial analysis. The system operates through a multi-agent debate and consensus mechanism, mirroring a high-stakes investment committee. Different specialized agents cross-examine each other to rigorously vet investment ideas, manage portfolio risk, and produce actionable research.

## 2. The Board Members (Agents)
The system is composed of eight specialized agents, each with a distinct identity, role, and set of directives:

*   **The Chairman (CFO):** The decisive leader of the boardroom. The Chairman enforces the Investment Policy Statement (IPS), actively cross-questions the other agents to uncover blind spots, synthesizes conflicting views, and has the absolute final say (Veto or Execution) on any trade.
*   **The Analyst (Fundamental Expert):** The classic fundamental investigator. Focuses on business quality by analyzing financial statements (ROCE, Cash Flow, Debt profile, Promoter quality). Checks if a company is a long-term "compounder."
*   **The Architect (Macro Strategist):** Analyzes the global cycle, macroeconomic "weather," liquidity conditions, and sector flows. Ensures that the overall economic environment is favorable before the board approves any stock.
*   **The Critic (Strategist & Auditor):** The value-investing skeptic. Defaults to "NO." Audits the business model strictly for a durable competitive advantage (moats), pricing power, safe valuation, and management integrity.
*   **The Engine (The Quant):** The data-driven backbone of the board. Provides cold, hard logic using technical indicators (RSI, Moving Averages) and fundamental valuation metrics. Strips away narratives to expose the mathematical reality.
*   **The Guardian (Risk Manager):** Focuses entirely on downside protection. Calculates portfolio impact, checking correlation matrices, sector exposure limits, and volatility constraints. Possesses absolute veto power on position sizing and exposure.
*   **The Hunter (Trend Scout):** The alpha narrative specialist. Scans news, social sentiment, and emerging themes to identify shifts before they show up in earnings reports. Pitches stories and defends trends against the Critic.
*   **The Presenter (Institutional Research Architect):** The lead buy-side analyst who aggregates the board's "Hard Intelligence." Instead of participating in the debate, the Presenter commands sub-agents to provide specific data to build high-fidelity, visual JSON Research Packs (e.g., Valuation Football Fields, Tear Sheets, Margin Waterfalls).

## 3. Standard Workflows
The system operates through three primary, predefined workflows, triggered via specific commands:

### `/portfolio` (The Portfolio Review)
A line-by-line performance and risk review of the current holdings.
1.  **Chairman:** Initiates the roll call and status.
2.  **Engine:** Calculates Total Return, Alpha, and identifies Winners/Losers.
3.  **Guardian:** Audits the current correlation and concentration risk.
4.  **Critic & Architect:** Re-evaluate the original thesis for losers and the macro environment for winners.
5.  **Chairman:** Issues final rebalancing orders (Maintain, Trim, or Sell).

### `/ticker <SYMBOL>` (The Deep Dive Audit)
An exhaustive, multi-dimensional audit of a specific stock proposed for investment.
1.  **Engine:** Pulls the raw financial data and technicals.
2.  **Analyst:** Reviews fundamentals and business quality.
3.  **Architect:** Checks the macro/sector tailwinds or headwinds.
4.  **Critic:** Attacks the company, presenting the "Bear Case" and Moat Audit.
5.  **Hunter:** Defends the stock, presenting the "Bull Case" and hidden alpha.
6.  **Guardian:** Simulates the trade's portfolio risk impact.
7.  **Chairman:** Reviews all inputs, synthesizes the debate, and renders the final `BUY/PASS` verdict.

### `/trendy` (The Trend Hunt)
A scouting workflow to discover and debate brand-new investment ideas.
1.  **Hunter:** Scans for emerging narratives and pitches 3 high-conviction ideas to the board.
2.  **Architect:** Immediately filters out any ideas facing severe macro headwinds.
3.  **Engine:** Pulls the hard data for the surviving ideas to ground the narratives in reality.
4.  **Chairman:** Reviews the dialogue and selects exactly *one* idea to push into the `/ticker` deep dive workflow, or dismisses them all.

## 4. Core Philosophy: Principle-Based Tension
The effectiveness of this agentic system lies in its designed friction. The Hunter brings optimism, the Critic applies pessimism, the Engine grounds discussions in pure data, and the Guardian tightly manages the risk. The Chairman, acting as the ultimate synthesizer, ensures that this "red teaming" approach allows only the highest-conviction ideas to survive the boardroom and execute.
