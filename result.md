# Results: it is the performace of this project on live trades 


> **Records Analysed:** 157

## 1. Overview


This report summarises the outcomes recorded in the supplied live dataset.

## 2. Live Results Summary

| Metric           | Count | Percentage |
| ---------------- | ----: | ---------: |
| Total Trades     |   157 |    100.00% |
| Take Profit (TP) |    58 |     36.94% |
| Stop Loss (SL)   |    69 |     43.95% |
| CTC              |    30 |     19.11% |

The dataset contains 157 recorded outcomes: 58 TP, 69 SL, and 30 CTC.

## 3. Buy vs Sell Results

| Direction |     TP |     SL |    CTC |   Total |
| --------- | -----: | -----: | -----: | ------: |
| Buy       |     31 |     35 |     17 |      83 |
| Sell      |     27 |     34 |     13 |      74 |
| **Total** | **58** | **69** | **30** | **157** |

Buy trades represented 52.87% of the records, while Sell trades represented 47.13%.

## 4. TP/SL Outcome Analysis

Excluding CTC records, 127 trades have either a TP or SL outcome.

| Outcome   |   Count | Percentage of TP/SL Trades |
| --------- | ------: | -------------------------: |
| TP        |      58 |                     45.67% |
| SL        |      69 |                     54.33% |
| **Total** | **127** |                **100.00%** |

The TP share among trades labelled TP or SL was 45.67%.

## 5. What These Results Tell Us

The recorded data shows that:

* 157 trade outcomes were logged.
* TP, SL and CTC outcomes are represented in the dataset.
* Both Buy and Sell trades were recorded.
* The dataset provides a starting point for reviewing real trading outcomes.

These figures describe the recorded sample only. They do not establish that the model caused the outcomes or improved trading performance.

## 6. Data Source

The analysis uses the supplied CSV containing these columns:

| Column       | Meaning                          |
| ------------ | -------------------------------- |
| `Image_Path` | Path to the recorded chart image |
| `Type`       | Buy or Sell direction            |
| `Result`     | Recorded TP, SL or CTC outcome   |


All 157 records contained values in the three required columns.


T

## 9. Conclusion

Model_12 has a dataset of 157 recorded live-trading outcomes 

Within this sample, 58 trades were labelled TP, 69 SL, and 30 CTC. The TP share among TP/SL-labelled trades was 45.67%.

These results provide a transparent summary of the recorded data. A conclusion about the model's actual predictive edge or profitability requires the original predictions and more complete trade-level performance data.

---

**Transparency Note:** This report describes the supplied live records. It does not present unverified accuracy claims or guarantee future trading results.
