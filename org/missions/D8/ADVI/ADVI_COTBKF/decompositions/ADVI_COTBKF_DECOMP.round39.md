# ADVI_COTBKF decomposition -- ROUND 39 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-09 ~13:4xZ)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2`'s CB-aj-2 CTO half AMENDMENT 1 @fa3cabc1ea (msg 3385). It places a COTBKF enrichment item: the cot gold
`_ff_worker` (`data/cot/scripts/gold/B_00.canonical_holdings.py`:1339-1378) is an UNFLAGGED stale-price carry-forward.
- It is unreachable for cot today: `schwab/silver/rps/` is empty, measured against a positive control.
- If that prefix fills, it would carry the removed bond prices forward with no claim field.
- The fix: the carry-forward stamps `price_basis: carried_forward` and the source date on every row it fills, OR skips any asset whose
  last price came from a non-firm source.
- It is a code change under COTBKF's own pair, not a rider on the round-36 rewrite. Round 38 (which holds ADDENDUM 11.2's cell) is
  already issued, so it is round 39.

**Rule 24.** Domain: one item -> one cell, the code change plus its test, LOCAL. Deploying the changed gold script is a SERVED act and
a later cell, under its own pair. The cell does not deploy.

## Measured constraints (issuer, ~13:4xZ)

1. `_ff_worker` (:1339) builds `hybrid_prices`:
   - today's `canonical_prices` rows where present;
   - otherwise the prior holdings file's `price` per `asset_name` (`fallback`, or the whole `prior_price_lookup` when the day is
     empty).
   - It then calls `price_holdings(ph, hybrid_prices)`.
   - A carried price is indistinguishable from a fresh one in the output. The only trace is a log line when more than 10% is carried.
2. The holdings rows carry a `source` column (`src_counts = ph['source'].value_counts()`). Which value a carried row receives is
   unmeasured.
3. Existing tests: `data/cot/scripts/gold/tests/` (e.g. `test_b00_carries_cusip_and_cash_flag.py`).

## The cells

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-am-1` | `_ff_worker` stamps every carried price with a claim (`price_basis=carried_forward` plus the source date) and never carries a price whose source is another firm's label; test included; no deploy | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~67` |

**Fan-out:** `1 of 1 chains, cap 8`.
