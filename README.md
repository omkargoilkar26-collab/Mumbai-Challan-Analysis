# Mumbai Traffic Challan Analysis (2024)

Analysis of 2024 traffic challan and violation data across 91 Mumbai police stations, covering how much of the fine money is actually collected and what kinds of violations are being enforced.

> **Disclaimer:** This is an independent analysis of publicly available data. It is not affiliated with or endorsed by the Mumbai Traffic Police.

---

## The question

**Is Mumbai's traffic enforcement collecting what it issues, and is it targeting the behavior that causes the most harm?**

### Supporting questions

**Collection (fines table)**
1. What share of challans and rupees goes unpaid, citywide and per station?
2. Are unpaid tickets larger fines than paid ones?
3. How concentrated is the unpaid money in the top 10 stations?
4. Is non-payment uniform, or do smaller stations collect better than larger ones?

**Enforcement (violations table)**
5. Which violation types dominate citywide?
6. Do stations differ in their most common violation?
7. How much enforcement goes to high-risk behavior compared with procedural offenses?

---

## Data

Public Mumbai traffic data for 2024. Source: [[FILL: source URL]]

| File | Used | Notes |
|---|---|---|
| Police station-wise challans and fines | Yes | Total, paid and unpaid challans and amounts per station |
| Total violations by police station | Yes | Count of each of ~24 violation types per station |

Both source tables include a "Grand Total" row, which was removed before any station-level or citywide calculation.

---

## Tools

- **Python (Pandas, NumPy)**: cleaning, aggregation, feature engineering
- **SQL (SQLite via SQLAlchemy)**: window functions, CTEs, ranking
- **Power BI**: data model, DAX measures, interactive dashboard

---

## Key findings

### 1. Non-payment is citywide, not a few bad stations
- **Insight:** 695K of 848K challans (81.96%) and ₹550M of ₹671M (82.06%, about ₹55 crore of ₹67.1 crore) are unpaid. Each of the ten highest-volume stations has an unpaid rate above 74%. Malwani, the highest-volume station (48,637 challans), has the highest unpaid rate among them at 92.25%.
- **So what:** Issuing challans is not translating into collection anywhere in the city, so the problem is systemic.
- **Action:** Look at payment friction citywide (reminders, payment channels, escalation after a deadline), starting with the high-volume stations where the most money is stuck.

### 2. Unpaid money is concentrated in a few stations
- **Insight:** [[FILL: top 10 stations hold X% of all unpaid money (₹Y M of ₹550M)]]
- **So what:** [[FILL]]
- **Action:** [[FILL: e.g. a targeted recovery drive at these stations]]

### 3. Unpaid vs paid ticket size, and station size vs non-payment
- **Insight:** [[FILL: average unpaid fine vs average paid fine; small / medium / large station unpaid rates]]
- **So what:** [[FILL]]

### 4. Enforcement is concentrated on one offense
- **Insight:** Riding without a helmet is 52.73% of all violations (447,069). The top three categories (helmet, "Other M.V. Acts", obstruction to traffic flow) are about 88% of everything. Drunk driving, speeding and wrong-side driving do not appear among the ten most common violation types citywide.
- **So what:** Enforcement volume follows the offenses that are easiest to observe and record. Offenses that need active patrols or testing barely register.
- **Action:** Review whether enforcement capacity is being steered toward high-severity offenses, or whether the data simply reflects how hard they are to detect.

### 5. Stations differ, but not on the dangerous offenses
- **Insight:** The most common violation is helmet at 60 of 91 stations, "Other M.V. Acts" at 21, and obstruction at 10. No station's most common violation is drunk driving, speeding or wrong-side driving.
- **So what:** Local enforcement character does vary (for example obstruction dominates at Dharavi and Azad Maidan), but the variation is between low-severity categories.

### 6. Risk profile of enforcement
Violations were grouped into three buckets. The grouping is an analyst judgment, not an official classification.

| Bucket | Violations included | Share of all violations |
|---|---|---|
| [[FILL: crash-causing]] | [[FILL: columns]] | [[FILL: %]] |
| [[FILL: injury-mitigation]] | [[FILL: columns]] | [[FILL: %]] |
| Procedural / other | [[FILL: columns]] | [[FILL: %]] |

- **Insight:** [[FILL: outlier station and how many times the citywide rate, computed under this same grouping]]
- **So what:** [[FILL]]

---

## Dashboard

![Page 1: Collection overview](images/dashboard_page1.png)
![Page 2: Enforcement and risk](images/dashboard_page2.png)

The Power BI file is in `powerbi/`. Features: station slicer, citywide and per-station KPIs, paid vs unpaid breakdown, top violation types, challan volume vs unpaid rate by station.

---

## Method notes

- Citywide rates use the sum of the numerator divided by the sum of the denominator, not an average of station-level rates, so large stations carry their real weight.
- The "Grand Total" row was removed by label, not by position, so the filter does not depend on sort order.
- Station-level shares (for example the share of each station's own violations) are used instead of raw counts when comparing stations of different sizes.
- Reconciliation checks: paid plus unpaid equals total for challans and amounts, and the violations table total matches the fines table total (about 848K).

---

## Limitations

- **One year only (2024).** There is no time dimension, so trends and seasonality cannot be analyzed.
- **Challans are enforcement records**, not a count of all violations that actually occurred.
- **"Other M.V. Acts" is an unspecified catch-all** and the second-largest category (19.17%). Nothing specific can be said about what it contains.
- **The risk grouping is a judgment call**, and the headline share changes depending on which violations are placed in each bucket.
- **Findings show association, not cause.**

---

## Repository structure

```
mumbai-traffic-analysis/
├── README.md
├── ingestion_db.py        # loads the CSVs into a local SQLite database
├── data/                  # source CSVs
├── notebooks/             # analysis notebook
├── powerbi/               # .pbix dashboard
```

## How to run

1. Clone the repo and install dependencies: `pip install pandas numpy sqlalchemy jupyter`
2. Keep the CSVs in the paths the notebook expects.
3. Open the notebook and run the cells top to bottom. `ingestion_db.py` builds the local SQLite database (`traffic.db`) on the first run.

---

## Next steps

- Join the fines and violations tables on station name to test whether what a station enforces relates to how much of its fines get paid.
- Add a time dimension if monthly data becomes available.
- Bring in vehicle registration data at the RTO level for a separate city-level analysis.

---

## Author

**Omkar Goilkar**: LinkedIn: https://www.linkedin.com/in/omkargoilkar/ | Github: https://github.com/omkargoilkar26-collab
