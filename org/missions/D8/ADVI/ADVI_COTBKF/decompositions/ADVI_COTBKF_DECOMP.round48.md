# ADVI_COTBKF decomposition -- ROUND 48 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-09 ~15:3xZ)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2`'s ADDENDUM 20 @3a563d35b1 (msg 3565). Round 45 is MET. On W72-S1 the CTO says YES: sweep
`commonwealth_bd_txn_provenance.py`:37 and the cot writer :65 with the validated `legacy_addresses` rows. The :103 regex is not a key
and is left alone.
- The writer is deployed, so its edit goes under its own pair: the census is the writer only, registry first if a row is added.
- The cell's grep covers EVERY COTBKF script and expects 0.

**Rule 24.** Domain: one item -> one cell, WORLD per the gate floor for a registry path (the code sweep and its repo-wide grep test). The writer's redeploy is a later SERVED
cell under its own pair. It is batched with round 46's writer change, and both ride ONE redeploy of the writer, registry first.

## Measured constraints (issuer, ~15:3xZ)

1. **The writer `data/cot/scripts/gold/build_canonical_prices_v2.py` is being edited NOW by round 46's ~73** (CB-at-1, input
   resolution). This cell edits the same file, so it depends on CB-at-1's drain and is spawned after it.
2. The rows `<own>-silver-prices-prefix` and `<own>-code-gold-scopes-pin` exist in `infra/logic/registry/legacy_addresses.json`
   (round 45; `validate` OK at registry@f936f6350cc5c404).
3. **"Every COTBKF script":** this project's scripts are `data/assets/scripts/silver/commonwealth_*.py` and the cot gold writer and
   holdings builder this project changed (`build_canonical_prices_v2.py`, `B_00.canonical_holdings.py`). The cell prints its
   denominator.

## The cells

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-av-1` | sweep the split key literals at provenance :37 and writer :65 onto the `legacy_addresses` rows; a repo-wide ast grep over every COTBKF script expects 0; no deploy | FWD-3 | WORLD | CB-at-1 (same writer file) | `0.9.0_WK_ADVI_COTBKF~75` |

**Fan-out:** `1 of 1 chains, cap 8`. The spawn is gated on round 46's drain.
