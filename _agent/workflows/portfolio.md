---
description: Trigger the /portfolio workflow for a line-by-line review.
---
# WORKFLOW: THE PORTFOLIO REVIEW

## 1. THE ROLL CALL (Chairman)
The user has invoked `/portfolio`.
- **Step 1:** @Chairman, load `current_portfolio.csv` (if it exists).
- **Action:** "Board, report status. Are we winning?"

## 2. THE PERFORMANCE CHECK (Engine)
- **Step 1:** @Engine, calculate the **Total Return** and **Alpha vs. SPY**.
- **Action:** Identify the **Winner** (best performer) and the **Loser** (worst performer).
- **Output:** "Portfolio is UP/DOWN [X]%. Best: [TICKER]. Worst: [TICKER]."

## 3. THE RISK AUDIT (Guardian)
- **Step 1:** @Guardian, check the **Correlation Matrix**.
- **Action:** Are we too concentrated? Is any position > 15% (IPS Violation)?
- **Output:** "Risk Levels: [Stable/Critical]. Action Required: [None/Rebalance]."

## 4. THE THESIS CHECK (Critic & Architect)
- **Step 1:** @Critic, pick the **Loser** stock. Does the original thesis still hold?
- **Step 2:** @Architect, is the macro environment still favorable for our **Winner**?
- **Output:** "Sell [Loser]?" / "Trim [Winner]?"

## 5. THE REBALANCE ORDER (Chairman)
- **Step 1:** @Chairman, issue final orders.
- **Action:** "Maintain Course" OR "Issue Sell Order for [TICKER]."
