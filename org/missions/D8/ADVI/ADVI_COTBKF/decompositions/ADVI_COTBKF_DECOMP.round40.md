# ADVI_COTBKF decomposition -- ROUND 40 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-09 ~13:5xZ)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2`'s ADDENDUM 12 @7d33a8581d (msg 3390), the ruling on D2-S62: the cross-firm test keys on a FIRM FIELD,
never a token.
- Every price row carries `source_firm`, set by the writer from its INPUT's address (bucket and key prefix), never from a name or
  ticker token.
- The check reads `source_firm != cottonwood` as a breach. A missing field is `absent`, which grades NOT-CLEAN.
- The cell: add `source_firm` at the cot price writer (`build_canonical_prices_v2.py`) and to the rewrite census.
- The 38 rewritten keys are not re-minted. The field arrives with the next silver-prep under its own pair.

**Mapping to the CTO's round-38 enrichment list:**

| CTO item | issued as |
|---|---|
| 1. `account_return_daily` | round 38, CB-al-1/2 |
| 2. `_ff_worker` flag | round 39, CB-am-1 (amended to the field rule @f12d8d0507) |
| 3. `source_firm` | THIS round |
| 4. bonds' firm-owned price | round 37, CB-ak-1 (graded MET, D2-S61) |

One issuance per round is gate-enforced, so each later item is its own round.

**Rule 24.** Domain: one item -> one cell, code plus tests, LOCAL, no deploy. The deploy and the next silver-prep come later, under a
pair.

## Measured constraints (issuer, ~13:5xZ)

1. `data/cot/scripts/gold/build_canonical_prices_v2.py` assembles `canonical[['date', 'asset_name', 'ticker', 'price', 'source']]`
   (:565) and writes `silver/prices/canonical_prices.parquet` (:624; CB-aj-1 census). `source` is a provenance LABEL
   (`yahoo_finance`, `linear_interpolation`, `transaction_observed`, ...). It is not a firm.
2. The rewrite census is in `data/assets/scripts/silver/commonwealth_cot_price_rewrite.py` (CB-aj-1).
3. Round 39's `_ff_worker` change carries `source_firm` through, with absent reading `"absent"`. This round makes it present.

## The cells

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-an-1` | `source_firm` on every row the cot price writer emits, from each row's INPUT address via `lib/opal_naming`; the rewrite census reads it (absent = NOT-CLEAN); tests; no deploy | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~68` |

**Fan-out:** `1 of 1 chains, cap 8`.
