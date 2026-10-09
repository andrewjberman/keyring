# ADVI_COTBKF: remediations, round 33

<sweep_watermark>2026-10-09T10:50Z</sweep_watermark>

Graduated at round 33's L9 (ADJUDICATION_v26.md), round label v34: D2-S50 (BLOCKING) and W60-S1, OPEN.

```json
[
 {
  "id": "ADVI_COTBKF-D2-S50",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "The SERVED FWD-3 tables rest materially on dividend-adjusted prices: in account_day_value, 638,948 of 1,669,040 account-days (38.3%), 688 of 1,528 accounts and 31,249 of 81,718 account-months (73 of 159 months) hold at least one position priced from a dividend_adjusted or mixed ticker, while the chain also books dividends as cash. Until CTO ADDENDUM 8 item 2's marking and rebuild land, a reader of those served rows sees values on the wrong basis with no mark.",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-S50",
   "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_33_DRAIN_END_20261009.md @2fc7789480 (served-table counts, the issuer's run equal to the worker's)"
  ],
  "remedy": "Mark every served account_day_value / daily_returns / month_grades row resting on a dividend_adjusted or mixed ticker (ADDENDUM 8 item 2) at once, then rebuild on as-traded Close with dividends as cash (method_r33, CB-ag-2) and re-mint under a pair (CB-ag-3); re-grade.",
  "owner": "2.0.0_SA_COO~C2",
  "round": "v34",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~C2",
   "round": "v34"
  },
  "closed": false
 },
 {
  "id": "ADVI_COTBKF-D2-W60-S1",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The only repo code that writes the bd_txn_price label is in the bd firm's tree (data/black_diamond/scripts/silver/inject_scoped_overrides.py:136 default, force_source set at scoped_price_exceptions.json:10,18,26); no writer in data/cot, yet the cottonwood price store carries its 1,623 rows on 3 CUSIP_ tickers.",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-W60-S1",
   "git grep -n -F bd_txn_price -- '*.py' '*.json' at worktree HEAD e5b8ad94ba: 8 hits; writer = data/black_diamond/scripts/silver/inject_scoped_overrides.py:136 (src = exc.get('force_source', 'bd_txn_price')); the label values come from data/black_diamond/scripts/silver/scoped_price_exceptions.json lines 10, 18, 26; data/cot/scripts/gold/B_01.holdings_lots.py:2263 mentions it in a comment only"
  ],
  "remedy": "Rule whether bd_txn_price rows in opal-data-cot come from the shared Black Diamond platform's scoped exceptions (permitted) or another firm's pipeline (the cross-firm NEVER); read the writer's history (inject_scoped_overrides.py and the exceptions file) to decide.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v34",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v34"
  },
  "closed": true
 }
]
```
