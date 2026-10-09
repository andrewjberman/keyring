# ADVI_COTBKF decomposition -- ROUND 46 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-09 ~15:1xZ)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2`'s ADDENDUM 19 @47529c9d9e (msg 3547). Round 42 is MET. The ruling, on `parents[3]` path resolution:
- ONE LOCAL cell: every input the writer reads resolves FIRST beside the module (where the deployed registry sits), then at the repo
  root.
- Each input's resolved path is printed in the census.
- Any further repo-file input ships beside the writer, registry first, under its own pair.
- D2-S62's closing census must print the resolved path of every input. `absent` caused by path resolution is NOT the close; it is this
  cell's failure.

**Rule 24.** Domain: one item -> one cell, LOCAL.
- The writer change (`build_canonical_prices_v2.py`, deployed @GAOI7tOR; redeploying the change is a later SERVED cell, registry
  first).
- The census print (`commonwealth_cot_price_rewrite.py`).

## Measured constraints (issuer, ~15:1xZ)

1. The writer's repo-file input `lib/ticker_overrides.py` resolves through `Path(__file__).resolve().parents[3]` (:189). The writer
   also IMPORTS `from lib.ticker_overrides import YF_OVERRIDES, TICKER_CORRECTIONS` (:59). From `code/gold/`, with no `lib/` beside
   it, that import's behaviour at run time is unmeasured; the cell measures it.
2. **The census file is being edited by round 45's ~72 now** (CB-as-1, split literals). This cell edits the same file, so it depends
   on CB-as-1's drain and is spawned after it, never in parallel.
3. The census reads served price rows. To print each input's resolved path, the writer must record those paths in its output. This
   cell stamps them into the parquet's schema metadata, and the census prints them back.

## The cells

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-at-1` | the writer resolves every input beside the module first, then at the repo root; records each input's resolved path in the output's parquet metadata; the census prints them; tests | FWD-3 | LOCAL | CB-as-1 (same census file) | `0.9.0_WK_ADVI_COTBKF~73` |

**Fan-out:** `1 of 1 chains, cap 8`. The spawn is gated on round 45's drain.
