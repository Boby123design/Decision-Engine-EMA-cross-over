# Result.md — Experimental Results & Evaluation

## 1. Experiment Overview
The objective of this experiment is to evaluate the predictive edge and performance of the model on real-market live trades.

## 2. Dataset Details
* **Data Source:** Live trading outcomes logged via CSV (features include `Image_Path`, `Type`, `Result`).
* **Size:** 157 recorded live trades (83 Buy, 74 Sell).
* **Date Range:** Live execution forward-testing period.
* **Split Methodology:** 100% Live Test Set (Train/Validation splits were utilised in earlier development phases).

## 3. Model / Version
* **Model Name:** crossovervision-ai
* **Version:** Live-Production-v1
* **Checkpoint:** Latest live deployment checkpoint.

## 4. Baseline Comparison
* Comparing the `crossovervision-ai` candidate model against a standard baseline algorithmic strategy to measure improvements in false-signal filtering and win rate.

## 5. Evaluation Metrics
* **Total Trades Analysed:** 157
* **Take Profit (TP):** 58 (36.94% of total)
* **Stop Loss (SL):** 69 (43.95% of total)
* **Cost-to-Cost (CTC):** 30 (19.11% of total)
* **Effective Accuracy (Win Rate excluding CTC):** 45.67%

## 6. Visual Results
* **Charts & Screenshots:** Visual documentation of trade setups, entries, and exits are captured and mapped via the `Image_Path` directory for manual review of TP vs. SL setups. 

## 7. Trading Metrics
* **Risk-to-Reward Ratio:** Predefined per execution strategy limits (standardised across the 127 closed TP/SL trades).
* **Costs:** Factored into the 30 trades closed at breakeven (CTC).
* **Expectancy & Drawdown:** To be calculated using the exact pip/point values of the 58 TP and 69 SL trades.

## 8. Reproducibility & Conclusion
* **Configuration:** Analysis relies on the supplied CSV dataset with standard data extraction scripts. 
* **Conclusion:** The `crossovervision-ai` model processed 157 live outcomes, securing 58 Take Profits and 69 Stop Losses, resulting in an effective win rate of 45.67% on closed trades. The dataset provides a transparent foundation for reviewing real trading outcomes and refining the model's predictive edge.
