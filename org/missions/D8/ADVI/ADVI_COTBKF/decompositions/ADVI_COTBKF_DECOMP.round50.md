# ADVI_COTBKF decomposition -- ROUND 50 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-09 ~16:0xZ)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2`'s ADDENDUM 22 (msg 3620, D2-S72 BLOCKING, W75-S1) together with ADDENDUM 21 (D2-S71).

ADDENDUM 22:
- B_00 and the writer resolve their OWN firm from the pinned `scopes.json` beside them, with NO run-time `opal_naming` import.
  Fail-closed: `scopes.json` missing, or lacking the firm, STOPS the run before any write.
- **Every key the code writes stays the legacy pipeline's own constant** (rule 30 non-application, R19). No address is built at run
  time.
- B_00 and the writer redeploy under ONE pair, with:
  - the D2-S71 fail-closed restore;
  - `ticker_overrides` beside the writer (ADDENDUM 21).
- The census shows exactly B_00, the writer and the files beside them.
- Proof on the SERVED files: a synthetic rps-filled day runs `_ff_worker` with no ImportError; negative arm: `scopes.json` absent
  means STOP, 0 rows.

ADDENDUM 21: a missing or unreadable `ticker_overrides` STOPS before any write; the empty default and the WARN path are deleted. The
file ships beside the writer, pinned to its blob, BEFORE the writer, and is resolved beside the module first. Proof: 757 overrides
load; negative arm: the file absent means STOP, 0 rows.

**Rule 24.** Domain: one item (the redeploy of the cot gold code to a fail-closed, `opal_naming`-free state) -> two cells:
- `CB-ax-1`, LOCAL: the code and its tests;
- `CB-ax-2`, SERVED: the one-pair redeploy.

## Measured constraints (issuer, ~16:0xZ)

1. **The writer** `build_canonical_prices_v2.py` imports `from opal_naming import legacy_address, lookup` at module level (:115).
   Its S3 keys are built at run time from `legacy_address()` rows (:112-122, round 48).
   - ADDENDUM 22 reverses that for run time: the keys become the legacy pipeline's constants, plainly typed and NOT split (the round-48
     test `test_cotbkf_no_split_key_literals.py` stays green).
   - If the naming gate refuses a plainly typed legacy key, that is an R20 case to NAME, never a bypass.
2. **The live B_00** imports `opal_naming` inside `_ff_worker` (:1362-1365).
3. **The deployed mirror today:**

   | key | state |
   |---|---|
   | `code/gold/scopes.json` | present (VersionId `7ChC4J0G...`, blob 261c0cf8, round 42) |
   | `code/gold/lib/ticker_overrides.py` | present (the old import path) |
   | `code/gold/ticker_overrides.py` | absent |
   | `code/gold/build_canonical_prices_v2.py` | VersionId `GAOI7tOR...` (round 42) |
   | `code/gold/B_00.canonical_holdings.py` | VersionId `hU7ZrZTD...` (round 41) |

4. `schwab/silver/rps/` = 0 keys (round 42 drain, with a positive control). The live path is unreached.

## The cells

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-ax-1` | B_00 + writer: own firm from beside `scopes.json` (no run-time `opal_naming`); keys as plain legacy constants; `ticker_overrides` fail-closed; tests incl. a synthetic rps day and the scopes-absent and overrides-absent STOP arms | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~77` |
| `CB-ax-2` | ONE redeploy under ONE pair: `ticker_overrides.py` (and `scopes.json` if its blob changed) FIRST, then the writer and B_00; census exactly those; proof on the served files | FWD-3 | SERVED | CB-ax-1, both pair halves | `0.7.0_AE_CloudOps~CB2` |

**Fan-out:** `1 of 2 chains now, cap 8`.
