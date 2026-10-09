# ADVI_COTBKF decomposition -- ROUND 45 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-09 ~15:0xZ)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2`'s ADDENDUM 17 @809d6830ac (msg 3519), the ruling on D2-S67. The split literals in
`data/assets/scripts/silver/commonwealth_cot_price_rewrite.py` (`'pri' + 'ces'` near :76, and `'scopes' + '.json'` near :251) are a
rule-30 workaround and are REMOVED, in this order:
1. Import the owning pipeline's constant where one exists.
2. Otherwise add a registry row and take `address()`.
3. If the legacy shape is inexpressible, name the R20 departure for Andrew, and read the key only through an imported constant until he
   acknowledges.

The cell's test greps for split key literals and expects 0.

**Rule 24.** Domain: one item -> one cell (WORLD: it may add an infra/logic/registry row, which the gate floors at WORLD).

## Measured constraints (issuer, ~15:0xZ)

1. **The owning writer has NO module-level constant for the key.** `data/cot/scripts/gold/build_canonical_prices_v2.py`:746 types
   `output_key = 'silver/prices/canonical_prices.parquet'` inside a function. Its `_SILVER` (:65) is itself built
   `'/'.join(['silver', ''])`.
   - **The writer is NOT edited in this cell.** Round 42 (CB-ap-2) is deploying it NOW at sha256 `3ac0a502...`, and the pair says a
     later commit to the writer is not covered. Promoting a constant there would put the repo out of step with the just-served bytes.
     That is a separate cell after round 42 drains, if it is wanted.
2. **`code/gold/scopes.json`'s owner is the round-42 deploy definition** (an order, not a module). There is no constant to import.
3. **So both keys go to step 2 or 3:**
   - a registry row in `infra/logic/registry/` plus `address()` output;
   - or, if `address()` cannot express the legacy shape (bucket-root `silver/prices/...`, `code/gold/...`), a named R20 departure for
     Andrew.
4. Other scripts in this project use the same pattern, e.g. `PIN_KEY` from round 44 and the writer's `_SILVER`. The ruling names this
   script. The cell COUNTS the pattern in the project's other scripts and reports it as a row; it does not change them (no widening).

## The cells

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-as-1` | remove the split key literals from `commonwealth_cot_price_rewrite.py`; keys from a registry row + `address()`, or an R20 departure named; test greps for 0; other-file count reported | FWD-3 | WORLD | none | `0.9.0_WK_ADVI_COTBKF~72` |

**Fan-out:** `1 of 1 chains, cap 8`.
