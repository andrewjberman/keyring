# ADVI_COTBKF: remediations, round 40

<sweep_watermark>2026-10-09T14:16Z</sweep_watermark>

Graduated at round 40's L9 (ADJUDICATION_v31.md), round label v41: 2 rows, OPEN.

```json
[
 {
  "id": "ADVI_COTBKF-D2-W68-S2",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "CB-an-1: build_canonical_prices_v2.py now resolves every input's firm through lib/opal_naming (the repo-root lib/ and infra/logic/registry/). gold_dispatch.sh syncs only s3://<bucket>/code/gold/ into the script folder, so on that path the module or the registry may be absent. The writer then prints a WARN and stamps every row 'absent' (never the own firm); the repo-file input lib/ticker_overrides.py, resolved by its repo-relative path, also reads absent there. Three further facts for L9: (1) the naming gate REFUSED the first commit because moving the two existing silver key literals (transactions, historical_prices) into the INPUT_ADDRESSES dict touched them under the live remediation ADVI_FIRMBKTS, so the dict joins the tier folder from parts (_SILVER, the sibling-script pattern) rather than typing the literals; (2) the stamp is the firm of the input that supplied the row's price (transactions for T1, silver/historical_prices for T2); (3) the config inputs (ticker_lookup, ticker_overrides) are resolved and printed with a WARN when they differ, not folded into the stamp.",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-W68-S2",
   "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_40_DRAIN_END_20261009.md @5006e7df0d (msg 3433)"
  ],
  "remedy": "The deploy cell for build_canonical_prices_v2.py ships lib/opal_naming and infra/logic/registry/ beside it (gold_dispatch.sh syncs only code/gold/), and its after-read census shows cottonwood rows, not absent.",
  "owner": "2.0.0_SA_COO~C2",
  "round": "v41",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~C2",
   "round": "v41"
  },
  "closed": false
 },
 {
  "id": "ADVI_COTBKF-D2-W68-S1",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "CB-an-1: Step 5b of data/cot/scripts/gold/build_canonical_prices_v2.py selects T1 rows with source == 't1_transaction_observed', but resolve_prices_for_asset emits 'transaction_observed' and 'transaction_observed_capped' only; 't1_transaction_observed' appears once in the file, in that filter. The denomination check (a FATAL raise on a ratio over 10x or under 0.1x) therefore always sees an empty frame and prints nothing. Not changed (outside the order).",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-W68-S1",
   "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_40_DRAIN_END_20261009.md @5006e7df0d (msg 3433)"
  ],
  "remedy": "Step 5b's share-class check filters on 't1_transaction_observed', a source the writer never emits, so it never runs: fix the label to what resolve_prices_for_asset emits (or remove the check) with a test that makes it fire.",
  "owner": "2.0.0_SA_COO~C2",
  "round": "v41",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~C2",
   "round": "v41"
  },
  "closed": false
 }
]
```
