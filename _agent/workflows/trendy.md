---
description: Trigger the /trendy workflow to scout and debate new investment ideas.
---
# WORKFLOW: THE TREND HUNT

## 1. THE HUNT (Hunter)
The user has invoked `/trendy`.
- **Step 1:** @Hunter, you are up. Scan your sources (TechCrunch, Reddit, Twitter/X, Financial News) for **Emerging Narratives**.
- **Step 2:** List **10 Trending Tickers** or Themes.
- **Step 3:** Filter them down to **3 High-Conviction Ideas** based on "Alpha" potential.
- **Action:** Present these 3 ideas to the Boardroom with a 1-line "Hook" for each.

## 2. THE MACRO FILTER (Architect)
- **Step 1:** @Architect, review the 3 ideas.
- **Action:** Kill any idea that fights the current "Macro Weather" (e.g., "Kill the Solar stock, rates are too high").
- **Output:** Explain WHY you are killing it or letting it pass.

## 3. THE REALITY CHECK (Engine)
- **Step 1:** @Engine, for the surviving ideas, pull the **HARD DATA**.
- **Action:** Post the [QUANT DATA] block for each.
- **Output:** Flag any valuation that is "Insane" (e.g., P/E > 100 with no growth).

## 4. THE CHAIRMAN'S SELECTION (Chairman)
- **Step 1:** @Chairman, review the dialogue.
- **Action:** Select **ONE** idea for a **DEEP DIVE** or **DISMISS ALL**.
- **Output:**
    - If DISMISS: "Board, these are all garbage. Back to work." -> END WORKFLOW.
    - If SELECT: "We will audit [TICKER]. Everyone, positions!" -> PROCEED TO `/ticker [TICKER]` WORKFLOW (Manual Trigger by User or Assistant).
