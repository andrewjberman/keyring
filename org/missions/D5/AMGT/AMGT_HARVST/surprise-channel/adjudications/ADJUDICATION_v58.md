# AMGT_HARVST ROUND 46 -- L8 COMPILE + L9 -- FWD-17 window union PASS (699 = 233 x 3); as-1 191 of 191; the named census now picks the served row; Z-W94-S1 DISARMED; L10 precondition MET

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-05 ~05:5xZ
**Input:** `2.0.0_SA_COO~H` `round46/ROUND46_DRAIN_END_PACKET.md` @`e51fb4ddac` (36 lines, read to EOF), msg 29500. It was drained on the CTO ruling @`7cd62976f1`. Every round-46 order is terminal, and the collection run continues across the boundary as signed.

## Read by this seat

| item | read | grade |
|---|---|---|
| FWD-17 window union (as-2) | `chatter_window/date=2026-10-04/part-20261005T011931Z`: 699 rows, 233 names x 3, tone null iff voters 0 on every row, 163 explicit zeros; the served chatter route's 95 covered names are all present | **PASS** |
| as-1 resolution | `rank_universe_identity_20260916.json`: 191 records, every one with an sa_symbol (TPG = `TPG`, status ISSUER) | **PASS** (mechanical, accepted) |
| as-3 census fix (Z-S85) | `round46/field_census.py:202-208`: `served_choice` returns `store.supersedes(...)`, the serving reader's rule | **PASS**: this closes v57's ask |
| collection outcomes (as-1b) | the run is in flight and the declared set is empty | **not gradeable**: round 47 reads the per-leg report; ft is held on Andrew's word |

## Rows

- `Z-W94-S1` (BLOCKING, ARMED): GRADUATED by this carrier and DISARMED in REMEDIATION_v7 on @`e379f86719`.
- `Z-W94-S2` and `Z-S86` are INERT, and both are ruled.

## L10 PRECONDITION

Every order is terminal. `comp-surprise --armed AMGT_HARVST` read 1 (Z-W94-S1) before REMEDIATION_v7. **MET.**

```json
[
 {
  "id": "AMGT_HARVST-Z-C-S78",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "surfaced_by": "3.0.0_SA_CVO~Z",
  "surfaced_at": "2026-10-05T05:55:00Z",
  "one_line": "Round 46 L8/L9: FWD-17 window union PASS -- chatter_window part-20261005T011931Z carries 699 rows = 233 names x 3, tone null iff voters 0 on every row, 163 explicit-zero rows, all 95 RESAPP covered names present; as-1 191 of 191 sa_symbol (TPG = TPG by issuer ruling R2b); as-3 census fix: served_choice = store.supersedes (field_census.py:208); collection outcomes not yet gradeable (run in flight, declared set empty).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "S3 opal-data-harvest amgt/harvest/gold/chatter_window/date=2026-10-04/part-20261005T011931Z.parquet: 699 rows, 233 names, 3 each",
    "lambda:Invoke /lead-panel/timeseries/collected/chatter?days=30: 95 covered names, 95 present in the table",
    "deliverables/0.9.0_WK_AMGT_HARVST~94/rank_universe_identity_20260916.json: 191 records, sa_symbol status DERIVED 153 / INFERRED 23 / MEASURED 14 / ISSUER 1",
    "deliverables/2.0.0_SA_COO_H/round46/field_census.py:202-208 served_choice -> store.supersedes"
   ]
  },
  "disposition": "GRADUATED",
  "adjudicates": [
   "AMGT_HARVST-Z-W94-S1"
  ],
  "spec_asserts": "FWD-17: gold carries, per covered name per window, articles_total, voters and tone.",
  "world_is": "233 names x 3 windows, explicit zeros where no coverage; the 21 RESAPP names that lacked rows now carry them.",
  "notes": "Z-W94-S1's remediation row is REMEDIATION_v7. The collection run (as-1b) is graded at round 47 from its per-leg report; ft is held on Andrew's word."
 }
]
```

-- 3.0.0_SA_CVO~Z
